from pydantic import BaseModel
from database.Dao import Dao
from database.DaoConstants import DaoConstants

# from database_session.DaoConstants import DaoConstants
# import database_session
from .room import Room
from .wrapper import frontEndWrapperRoom
from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse
from typing import List
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


# db_config = {
#     "host": DaoConstants.HOST,
#     "port": 3306,
#     "user": DaoConstants.USER,
#     "password": DaoConstants.PASSWD,
#     "database": DaoConstants.DATABASE,
# }


class OutputCapture:
    def __init__(self):
        self.contents = ""

    def write(self, text):
        self.contents += text

    def flush(self):
        pass  # In here you might want to implement some functionality to clear the contents if needed


startedWrite = False



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# database_session = database_session.Database(**db_config)
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


templates = Jinja2Templates(directory="static")

current_room = Room()  # Temporary change later

# List to store active WebSocket connections
active_connections: List[WebSocket] = []
active_rooms: dict[int: Room] = {}  # Different rooms have different states

dao_instance = Dao()


# # Connect to the database on startup
# @app.on_event("startup")
# async def startup_event():
#     database_session.connect()


# # Disconnect from the database on shutdown
# @app.on_event("shutdown")
# async def shutdown_event():
#     database_session.disconnect()


@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# @app.get("/test_db")
# async def test_db_connection():
#     data = database_session.select_query(DaoConstants.GET_PROPERTY_LIST, ())
#     print(data)


# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     active_connections.append(websocket)  # Add the new connection to the list
#
#     # Define a function that reads from the standard output and sends the output to the client via the WebSocket.
#     try:
#         while True:
#             data = await websocket.receive_text()
#             # Do something with the data
#             await broadcast_message(data)
#             old_stdout = sys.stdout
#             capturer = OutputCapture()
#             sys.stdout = capturer
#             if current_room != None:
#                 frontEndWrapperRoom(data, current_room)
#             sys.stdout = old_stdout
#             await broadcast_message(capturer.contents)
#
#     except Exception as e:
#         active_connections.remove(websocket)  # Remove the disconnected client
#         print('Error is ', e)


class UserInput(BaseModel):
    text: str


@app.get("/polling/data")
async def polling_user_input():
    data = dao_instance.select_query(DaoConstants.SELECT_LOGS_BY_ROOM_ID, (1,))
    print(data)
    message = ''.join([item[0].strip() + '\n' for item in data if item[0].strip() != ''])
    return {'message': message}




@app.post("/player_turn")
async def turn(user_input: UserInput):
    # if not current_room:
    print(user_input.text)
    frontEndWrapperRoom(user_input.text, current_room)
    return {'input': user_input}

async def broadcast_message(message: str):
    for connection in active_connections:
        await connection.send_text(f"Message text was: {message}")
# Command: uvicorn web_socket:app --reload
