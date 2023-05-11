# FastAPI import statements
from fastapi import FastAPI, Request, WebSocket
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
#from move import router as MoveRouter
from fastapi.templating import Jinja2Templates
from starlette.websockets import WebSocketDisconnect

from database.Dao import Dao
from database.DaoConstants import DaoConstants
import http.client
import ssl
import uvicorn
# Game Logic import statements
from service.monopoly_Instance import monopoly_Instance


app = FastAPI()


# app.include_router(MoveRouter, tags=["moves"], prefix="/game")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")


class Move(BaseModel):
    move: str

@app.get('/')
async def read_main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



# @app.post("/submit_move")
# async def submit_move(move: Move):
#     # Process the move using your existing Monopoly game logic
#     # Replace this function with your actual game logic
#     message = f'Player entered {move.move}'
#     a = game_start(move)
#     while a is not None:
#
#     return message

@app.websocket("/submit_move")
async def websocket_endpoint(websocket: WebSocket, move: Move):
    await websocket.accept()
    # room.add_player(websocket)
    # await room.broadcast(f"Player joined the room: {websocket.client.host}")
    try:
        while True:
            message = await websocket.receive_text()
            print(message)
            await print(message)
            # await room.broadcast(message)
    except Exception as e:
        print('Error is ', e)
        # room.remove_player(websocket)
        # await room.broadcast(f"Player left the room: {websocket.client.host}")

# @app.get()


@app.get("/getLogs", response_class=JSONResponse)
async def get_logs(request: Request, room_id: int):
    try:
        db=Dao()
        daoConst=DaoConstants()
        logs = db.select_all_query(daoConst.SELECT_LOGS_BY_ROOM_ID, (room_id,))
        log_messages = [log[0] for log in logs]
        return "\n".join(log_messages)
    except Exception as e:
        return f"An exception occurred: {str(e)}"

# if __name__ == "__main__":
#     context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
#     context.load_cert_chain(certfile="./tls/ca-cert.pem", keyfile="./tls/ca-key.pem")
#     uvicorn.run(app, host="0.0.0.0", port=8443, ssl_context=context)

# How to replace stuff in the output area
# content = content.replace('<textarea id="output" readonly></textarea>', f'<textarea id="output" readonly>{moves}</textarea>')

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8443, reload=True, ssl_keyfile="./tls/ca-key.pem", ssl_certfile="./tls/ca-cert.pem")

