from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from typing import List

app = FastAPI()

# List to store active WebSocket connections
active_connections: List[WebSocket] = []

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


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)  # Add the new connection to the list

    try:
        while True:
            data = await websocket.receive_text()
            # cash and all
            # broadcast
            # do your input
            # Everything goes in here
            # a = game_start(data)
            await broadcast_message(data)  # Broadcast the message to all clients
    except Exception as e:
        active_connections.remove(websocket)  # Remove the disconnected client
        print('Error is ', e)


async def broadcast_message(message: str):
    for connection in active_connections:
        await connection.send_text(f"Message text was: {message}")
