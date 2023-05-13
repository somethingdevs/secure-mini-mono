# # FastAPI import statements
# from fastapi import FastAPI, Request
# from pydantic import BaseModel
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import JSONResponse
# #from move import router as MoveRouter
# from fastapi.templating import Jinja2Templates
# from database.Dao import Dao
# from database.DaoConstants import DaoConstants
# # Game Logic import statements
# from utils.driver import process_move
#
# app = FastAPI()
#
# app.include_router(MoveRouter, tags=["moves"], prefix="/game")
#
# app.mount("/static", StaticFiles(directory="static"), name="static")
# templates = Jinja2Templates(directory="static")
#
#
# class Move(BaseModel):
#     move: str
#
#
# @app.post("/submit_move")
# async def submit_move(move: Move):
#     # Process the move using your existing Monopoly game logic
#     # Replace this function with your actual game logic
#     result = process_move(move.move)
#     return {"message": result}
#
# @app.get("/getLogs", response_class=JSONResponse)
# async def get_logs(request: Request, room_id: int):
#     try:
#         db=Dao()
#         daoConst=DaoConstants()
#         logs = db.select_all_query(daoConst.SELECT_LOGS_BY_ROOM_ID, (room_id,))
#         log_messages = [log[0] for log in logs]
#         return "\n".join(log_messages)
#     except Exception as e:
#         return f"An exception occurred: {str(e)}"
#
# # How to replace stuff in the output area
# # content = content.replace('<textarea id="output" readonly></textarea>', f'<textarea id="output" readonly>{moves}</textarea>')
