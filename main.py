# FastAPI import statements
from uuid import UUID, uuid4
from pydantic import BaseModel
from fastapi import FastAPI, Request, Response, status, Depends
from fastapi_sessions.backends.implementations import InMemoryBackend
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
# from move import router as MoveRouter
from fastapi.templating import Jinja2Templates
from fastapi_sessions.frontends.implementations import SessionCookie, CookieParameters
from database.Dao import Dao
from database.DaoConstants import DaoConstants
from service.userHandle import UserHandle
from models.user import User
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import JSONResponse

from sessions.auth import encode_password, verify_password
from sessions.base_verifier import BasicVerifier
from sessions.core_types import SessionData

# Game Logic import statements

app = FastAPI()
cookie_params = CookieParameters()
backend = InMemoryBackend[UUID, SessionData]()

cookie = SessionCookie(
    cookie_name="cookie",
    identifier="general_verifier",
    auto_error=True,
    secret_key="DONOTUSE",
    cookie_params=cookie_params,
)

verifier = BasicVerifier(
    identifier="general_verifier",
    auto_error=True,
    backend=backend,
    auth_http_exception=HTTPException(status_code=403, detail="invalid session"),
)


class UserRegisterIn(BaseModel):
    username: str
    email: str
    password: str


class UserLoginIn(BaseModel):
    email: str
    password: str


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


@app.get("/getLogs", response_class=JSONResponse)
async def get_logs(request: Request, room_id: int):
    try:
        db = Dao()
        daoConst = DaoConstants()
        logs = await db.select_query(daoConst.SELECT_LOGS_BY_ROOM_ID, (room_id,))
        log_messages = [log[0] for log in logs]
        return "\n".join(log_messages)
    except Exception as e:
        raise Exception("Error in getting logs")


@app.post("/register")
async def register(user_input: UserRegisterIn):
    dao = Dao()
    _check = dao.insertion_query(DaoConstants.CREATE_USER, (user_input.username,
                                                   user_input.email,
                                                   encode_password(user_input.password)))
    print(_check)
    return {'message': 'success'}, 200


# @app.post("/login")
# async def login(user: UserLoginIn, response: Response):
#     dao = Dao()
#     _user = dao.select_query(DaoConstants.GET_USER, ('test@example.com',))
#
#     username = "something1"
#     password = "someting___random"
#
#     session = uuid4()
#     data = SessionData(username=username)
#     await backend.create(session, data)
#     cookie.attach_to_response(response, session)
#
#     # check = safe_str_cmp(_user[0][1], user.password)
#     # print(check)
#     return {}, status.HTTP_200_OK

@app.post("/login")
async def login(user: UserLoginIn, response: Response):
    dao = Dao()
    _user = dao.select_query(DaoConstants.GET_USER, ('hihi@gmail.com',))

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

