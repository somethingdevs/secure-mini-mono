# Standard library imports
from uuid import UUID, uuid4

import uvicorn
# Third-party libraries
from fastapi import FastAPI, Request, WebSocket, Response, status, Depends
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_sessions.backends.implementations import InMemoryBackend
from fastapi_sessions.frontends.implementations import SessionCookie, CookieParameters
from pydantic import BaseModel
from typing import List

# Local application imports
from sessions.auth import encode_password, verify_password
from sessions.base_verifier import BasicVerifier
from sessions.core_types import SessionData
from service.room import Room
from service.wrapper import frontEndWrapperRoom
from database.Dao import Dao
from database.DaoConstants import DaoConstants




app = FastAPI()
cookie_params = CookieParameters()
backend = InMemoryBackend[UUID, SessionData]()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")

cookie = SessionCookie(
    cookie_name="cookie",
    identifier="general_verifier",
    auto_error=True,
    secret_key="DONOTUSE",
    cookie_params=cookie_params,
)

verifier = BasicVerifier(
    identifier="general_verifier",
    auto_error=False,
    backend=backend,
    auth_http_exception=HTTPException(status_code=403, detail="invalid session"),
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "https://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UserRegisterIn(BaseModel):
    username: str
    email: str
    password: str


class UserLoginIn(BaseModel):
    email: str
    password: str


class UserInput(BaseModel):
    text: str

current_room = Room()

active_connections: List[WebSocket] = []
active_rooms: dict[int: Room] = {}  # Different rooms have different states

dao_instance = Dao()



@app.get("/login", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/", response_class=HTMLResponse , dependencies=[Depends(cookie)])
async def get(request: Request, session_data: SessionData = Depends(verifier)):
    if session_data is not None:
        return templates.TemplateResponse("room.html", {"request": request})
    else:
        return templates.TemplateResponse("login.html", {"request": request})


@app.get("/register", response_class=HTMLResponse)
async def get(request: Request):
        return templates.TemplateResponse("register.html", {"request": request})


@app.get("/whoami", dependencies=[Depends(cookie)])
async def whoami(session_data: SessionData = Depends(verifier)):
    return session_data


@app.post("/delete_session")
async def del_session(response: Response, session_id: UUID = Depends(cookie)):
    await backend.delete(session_id)
    cookie.delete_from_response(response)
    return "deleted session"


@app.post("/create_session/{name}")
async def create_session(name: str, response: Response):
    session = uuid4()
    data = SessionData(username=name)

    await backend.create(session, data)
    cookie.attach_to_response(response, session)

    return f"created session for {name}"


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "Internal server error"},
    )


@app.get("/getAllLogs", response_class=JSONResponse, dependencies=[Depends(cookie)])
async def get_all_logs(request: Request, session_data: SessionData = Depends(verifier)):
    try:
        db = Dao()
        daoConst = DaoConstants()
        logs = db.select_query(daoConst.GET_USER_LOGS, (session_data.username))
        return {"logs": logs}
    except Exception as e:
        raise Exception("Error in getting logs")


@app.post("/register")
async def register(user_input: UserRegisterIn):
    try:
        dao = Dao()
        _check = dao.insertion_query(DaoConstants.CREATE_USER, (user_input.username,
                                                    user_input.email,
                                                    encode_password(user_input.password)))
        print(_check)
        return {'message': 'success'}, 200
    except Exception as e:
        print(e)
        return {'message': 'failed to create user'}, 500

@app.post("/stats", response_class=JSONResponse, dependencies=[Depends(cookie)])
async def getStats(request: Request, session_data: SessionData = Depends(verifier)):
    try:
        db = Dao()
        daoConst = DaoConstants()
        winner_stats = db.select_query(daoConst.DISPLAY_WIN_LOSS, (session_data.username))
        #print(winner_stats[0][1])
        return {'stats':winner_stats[0][1]}, 200
    except Exception as e:
        raise Exception("Error stats", e)


@app.post("/login")
async def login(user: UserLoginIn, response: Response):
    dao = Dao()
    _user = dao.select_query(DaoConstants.GET_USER, (user.email))

    # print(_user)

    # Assuming _user[0][0] is the username and it's stored as a string
    username = _user[0][0]
    # Assuming _user[0][1] is the hashed password
    stored_password = _user[0][1]

    # print(verify_password(stored_password, user.password))

    if verify_password(stored_password, user.password):
        session = uuid4()
        data = SessionData(username=username)
        await backend.create(session, data)
        cookie.attach_to_response(response, session)
        return {}, status.HTTP_200_OK
    else:
        return {"error": "Invalid login credentials"}, status.HTTP_401_UNAUTHORIZED

@app.get("/maxroom", response_class=JSONResponse, dependencies=[Depends(cookie)])
async def getMaxRoom( request: Request, session_data: SessionData = Depends(verifier)):
    try:
            db = Dao()
            daoConst = DaoConstants()
           
            user_id = db.select_query(daoConst.GET_USER_ID, (session_data.username)) 
            user_id=user_id[0][0]
            maxRoom= db.select_all_query( daoConst.GET_MAX_ROOM,False)
            newroom=maxRoom[0][0]
            print(newroom)
            print('New Room count',maxRoom)
            return {'roomId':newroom+1},200

    except Exception as e:
        return {'msg':"Error fetching max room"},500



@app.get("/room/{room_id}", response_class=HTMLResponse, dependencies=[Depends(cookie)])
async def roomLogic(room_id: int, request: Request, session_data: SessionData = Depends(verifier)):
    try:
         db = Dao()
         daoConst = DaoConstants()
         print('In room')
         user_id = db.select_query(daoConst.GET_USER_ID, (session_data.username))
        
         user_id=user_id[0][0]
         print(user_id)
         isexistingRoom=db.select_query(daoConst.ROOM_EXIST,(room_id,))
         isexistingRoom=isexistingRoom[0][0]
         print(isexistingRoom, 'exists?')
         if isexistingRoom:
                #isexistingRoom=isexistingRoom[0][0]
                print('In join room')
                room_instance = Room()
                isAllowed=room_instance.join_row(room_id, user_id)
                if isAllowed:
                    print('Allowed go aheasd')
                    return templates.TemplateResponse("index.html", {"request": request, "room_id": room_id})

                else:
                    print('Not allowed to join room')
                    return templates.TemplateResponse("room.html", {"request": request}) #back to room
         elif not isexistingRoom:
            room_instance = Room()
            room_instance.createRoom(user_id, room_id=room_id)

            return templates.TemplateResponse("index.html", {"request": request, "room_id": room_id})

            
    except Exception as e:
        raise Exception("Error in getting logs", e)



# @app.get("/room/{roomID}", response_class=HTMLResponse, dependencies=[Depends(cookie)])
# async def get(request: Request, roomID: str,session_data: SessionData = Depends(verifier)):
#     return templates.TemplateResponse("index.html", {"request": request})

@app.get("/polling/data")
async def polling_user_input(room_id: int):
    print('Room id in get polling data', room_id)
    data = dao_instance.select_query(DaoConstants.SELECT_LOGS_BY_ROOM_ID, (room_id,))
    print(data)
    if data:
        message = ''.join([item[0].strip() + '\n' for item in data if item[0].strip() != ''])
    else:
        message = f'Welcome to room {room_id}, your match will begin shortly!'
    return {'message': message}




@app.post("/player_turn")
async def turn(user_input: UserInput, room_id: int):
    # if not current_room:

    print(user_input.text)
    print('Room ID in backend is ', room_id)
    frontEndWrapperRoom(user_input.text, current_room, room_id)
    return {'input': user_input}


@app.post("/logout")
async def logout(user: UserLoginIn, response: Response):
    dao = Dao()
    _user = dao.select_query(DaoConstants.GET_USER, (user.email))

    # print(_user)

    # Assuming _user[0][0] is the username and it's stored as a string
    username = _user[0][0]
    # Assuming _user[0][1] is the hashed password
    stored_password = _user[0][1]

    # print(verify_password(stored_password, user.password))

    if verify_password(stored_password, user.password):
        session = uuid4()
        data = SessionData(username=username)
        await backend.create(session, data)
        cookie.attach_to_response(response, session)
        return {}, status.HTTP_200_OK
    else:
        return {"error": "Invalid login credentials"}, status.HTTP_401_UNAUTHORIZED




# TLS/SSL
if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        ssl_keyfile=r"D:\Programming\SWE_681\secure-mini-mono\certificate\key.pem",
        ssl_certfile=r"D:\Programming\SWE_681\secure-mini-mono\certificate\cert.pem",
        ssl_keyfile_password="monopoly"
    )



