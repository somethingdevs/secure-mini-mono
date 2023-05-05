# FastAPI import statements
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
#from move import router as MoveRouter
from fastapi.templating import Jinja2Templates

# Game Logic import statements
from utils.driver import process_move

app = FastAPI()

app.include_router(MoveRouter, tags=["moves"], prefix="/game")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")


class Move(BaseModel):
    move: str


@app.post("/submit_move")
async def submit_move(move: Move):
    # Process the move using your existing Monopoly game logic
    # Replace this function with your actual game logic
    result = process_move(move.move)
    return {"message": result}

"""

@app.get("/", response_class=HTMLResponse)
async def serve_homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

"""

# How to replace stuff in the output area
# content = content.replace('<textarea id="output" readonly></textarea>', f'<textarea id="output" readonly>{moves}</textarea>')
