from service.room import room
from service.wrapper import frontEndWrapperRoom
from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse
from typing import List
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import sys
import io


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

templates = Jinja2Templates(directory="static")

# List to store active WebSocket connections
active_connections: List[WebSocket] = []
active_rooms: dict[int: room] = {}  # Different rooms have different states

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")

                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


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
