from fastapi import APIRouter
from fastapi.responses import FileResponse
from core.config import BASE_DIR
from core import schemas
import json

router = APIRouter()


@router.get('/user')
async def get_user_view():
    return FileResponse(BASE_DIR / 'user_server' / 'user.html')
    pass


@router.get("/items")
async def get_items() -> list[schemas.Item]:
    with open(f'{BASE_DIR}/db.json') as file:
        data = json.load(file)
    return [schemas.Item(**el) for el in data['products']]
