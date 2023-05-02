from pydantic import BaseModel
from fastapi import APIRouter, status

router = APIRouter()


class UserMove(BaseModel):
    move: str
