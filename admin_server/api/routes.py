from fastapi import APIRouter

from core import schemas
from core.config import BASE_DIR
import json

from fastapi.responses import FileResponse

router = APIRouter()


@router.get("/admin")
async def get_admin_page():
    return FileResponse(BASE_DIR/ "admin_server" / "admin.html")


@router.post("/items")
async def add_items(items: list[schemas.Item]):
    with open(f"{BASE_DIR}/db.json", "r") as file:
        data = json.load(file)

    data['products'].extend([el.model_dump() for el in items])
    with open(f"{BASE_DIR}/db.json", "w") as file:
        json.dump(data, file, indent=4)


@router.put('/items/{item_id}')
async def update_item(item_id: str, item: schemas.Item):
    with open(f"{BASE_DIR}/db.json", "r") as file:
        data = json.load(file)

    for i in range(len(data['products'])):
        if data['products'][i]['id'] == item_id:
            data['products'][i] = item.model_dump()
            break

    with open(f"{BASE_DIR}/db.json", "w") as file:
        json.dump(data, file, indent=4)


@router.delete("/items/{item_id}")
async def delete_item(item_id: str):
    with open(f"{BASE_DIR}/db.json", "r") as file:
        data = json.load(file)

    for i in range(len(data['products'])):
        if data['products'][i]['id'] == item_id:
            data['products'].pop(i)
            break

    with open(f"{BASE_DIR}/db.json", "w") as file:
        json.dump(data, file, indent=4)
