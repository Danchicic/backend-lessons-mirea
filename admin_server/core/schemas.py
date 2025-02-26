import uuid

from pydantic import BaseModel


class Item(BaseModel):
    id: str = uuid.uuid4().hex
    name: str
    description: str
    price: int
