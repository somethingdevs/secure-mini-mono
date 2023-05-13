from database.DaoConstants import DaoConstants
import database
from service.room import room
from service.wrapper import frontEndWrapperRoom
from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse
from typing import List
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import sys


db_config = {
    "host": DaoConstants.HOST,
    "port": 3306,
    "user": DaoConstants.USER,
    "password": DaoConstants.PASSWD,
    "database": DaoConstants.DATABASE,
}


class OutputCapture:
    def __init__(self):
        self.contents = ""

    def write(self, text):
        self.contents += text

    def flush(self):
        pass  # In here you might want to implement some functionality to clear the contents if needed


startedWrite = False


current_room = room()  # Temporary change later
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

database = database.Database(**db_config)


templates = Jinja2Templates(directory="static")

# List to store active WebSocket connections
active_connections: List[WebSocket] = []
active_rooms: dict[int: room] = {}  # Different rooms have different states


# Connect to the database on startup
@app.on_event("startup")
async def startup_event():
    database.connect()


# Disconnect from the database on shutdown
@app.on_event("shutdown")
async def shutdown_event():
    database.disconnect()


@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/test_db")
async def test_db_connection():
    data = database.select_query(DaoConstants.GET_PROPERTY_LIST, ())
    print(data)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)  # Add the new connection to the list

    # Define a function that reads from the standard output and sends the output to the client via the WebSocket.
    try:
        while True:
            data = await websocket.receive_text()
            # Do something with the data
            await broadcast_message(data)
            old_stdout = sys.stdout
            capturer = OutputCapture()
            sys.stdout = capturer
            if current_room != None:
                frontEndWrapperRoom(data, current_room)
            sys.stdout = old_stdout
            await broadcast_message(capturer.contents)

    except Exception as e:
        active_connections.remove(websocket)  # Remove the disconnected client
        print('Error is ', e)


async def broadcast_message(message: str):
    for connection in active_connections:
        await connection.send_text(f"Message text was: {message}")
# Command: uvicorn web_socket:app --reload
