import uuid
from typing import Optional

from pydantic import BaseModel


class Item(BaseModel):
    id: Optional[str] = uuid.uuid4().hex
    name: str
    description: str
    price: int
