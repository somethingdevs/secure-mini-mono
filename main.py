# FastAPI import statements
from fastapi import FastAPI, Request, status
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
#from move import router as MoveRouter
from fastapi.templating import Jinja2Templates
from database.Dao import Dao 
from database.DaoConstants import DaoConstants 
from service.userHandle import UserHandle
from models.user import User
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse 
# Game Logic import statements

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "Internal server error"},
    )

@app.get("/getLogs", response_class=JSONResponse)
async def get_logs(request: Request, room_id: int):
    try:
        db=Dao()
        daoConst=DaoConstants()
        logs = await db.select_query(daoConst.SELECT_LOGS_BY_ROOM_ID, (room_id,))
        log_messages = [log[0] for log in logs]
        return "\n".join(log_messages)
    except Exception as e:
        raise Exception("Error in getting logs")
    

@app.get("/register", response_class=JSONResponse)
async def register(request: Request, user_name: str,emailId:str,pwd:str):
    try:
       userrr=User( user_id=None,username=user_name,email=emailId, password=pwd)
       u=UserHandle()
       isSuccessfull=await u.createUser(userrr)
       if isSuccessfull:
        return "User Created"
       else:
        return("Unable to register")
    except Exception as e:
        return("Unable to register")
        #raise Exception("Unable to register")
    
@app.post("/login", response_class=JSONResponse)
async def login(request: Request,emailId:str,pwd:str):
    try:
       if emailId or pwd:
            print('Recieved Input',emailId,' , pwd= ',pwd)
            userrr=User( user_id=None,username=None,email=emailId, password=pwd)
            u=UserHandle()
            username= u.loginUser(userrr)
            if username:
                    value="Welcome back ",username
                    return value
       else:
        return "unable to login"
    except Exception as e:
        raise Exception("Unable to login")