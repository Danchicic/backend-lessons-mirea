from fastapi import APIRouter
from fastapi.responses import FileResponse
from core.config import BASE_DIR
from core import schemas
import json

from starlette.websockets import WebSocket

router = APIRouter()


@router.get('/user')
async def get_user_view():
    return FileResponse(BASE_DIR / 'user_server' / 'user.html')
    pass


@router.websocket("/ws")
async def chat(
        websocket: WebSocket,
):
    await websocket.accept()
    while True:
        user_text = await websocket.receive_text()
        print("user send", user_text)
