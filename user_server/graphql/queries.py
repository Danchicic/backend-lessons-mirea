import uuid

from strawberry.fastapi import GraphQLRouter
import strawberry
from typing import Optional
import datetime


def get_card_from_db(card_id):
    for el in database:
        if el['id'] == card_id:
            return el
    return None


database: list[dict] = [
    {
        "id": "8a5badb6cb374618aba887dbd8ddceca",
        "name": "updated card name",
        "description": "updated card description",
        "price": 123
    },
    {
        "id": "e7f5g6h89a0b1234ef56gh78ij90kl12",
        "name": "\u0418\u0433\u0440\u043e\u0432\u0430\u044f \u043a\u043e\u043d\u0441\u043e\u043b\u044c GameBox 5",
        "price": 49990,
        "description": "\u041d\u043e\u0432\u0430\u044f \u0438\u0433\u0440\u043e\u0432\u0430\u044f \u043a\u043e\u043d\u0441\u043e\u043b\u044c \u0441 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u043e\u0439 4K-\u0433\u0440\u0430\u0444\u0438\u043a\u0438 \u0438 \u043c\u043e\u0449\u043d\u044b\u043c \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440\u043e\u043c."
    },
    {
        "id": "f8g6h7i90a1b2345fg67hi89jk01lm23",
        "name": "\u041f\u043b\u0430\u043d\u0448\u0435\u0442 TabPro 10",
        "price": 45990,
        "description": "10-\u0434\u044e\u0439\u043c\u043e\u0432\u044b\u0439 \u043f\u043b\u0430\u043d\u0448\u0435\u0442 \u0441 Retina-\u0434\u0438\u0441\u043f\u043b\u0435\u0435\u043c \u0438 \u0431\u0430\u0442\u0430\u0440\u0435\u0435\u0439 \u043d\u0430 15 \u0447\u0430\u0441\u043e\u0432 \u0440\u0430\u0431\u043e\u0442\u044b."
    },
    {
        "id": "g9h7i8j01a2b3456gh78ij90kl12mn34",
        "name": "\u0423\u043c\u043d\u0430\u044f \u043a\u043e\u043b\u043e\u043d\u043a\u0430 SmartSound 2",
        "price": 11990,
        "description": "\u0413\u043e\u043b\u043e\u0441\u043e\u0432\u043e\u0439 \u0430\u0441\u0441\u0438\u0441\u0442\u0435\u043d\u0442 \u0441 \u043c\u043e\u0449\u043d\u044b\u043c\u0438 \u0434\u0438\u043d\u0430\u043c\u0438\u043a\u0430\u043c\u0438 \u0438 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u043e\u0439 Wi-Fi/Bluetooth."
    },
    {
        "id": "h0i8j9k12a3b4567hi89jk01lm23no45",
        "name": "\u0418\u0433\u0440\u043e\u0432\u0430\u044f \u043c\u044b\u0448\u044c ProGamer X",
        "price": 3990,
        "description": "\u0418\u0433\u0440\u043e\u0432\u0430\u044f \u043c\u044b\u0448\u044c \u0441 RGB-\u043f\u043e\u0434\u0441\u0432\u0435\u0442\u043a\u043e\u0439, 12 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u0443\u0435\u043c\u044b\u043c\u0438 \u043a\u043d\u043e\u043f\u043a\u0430\u043c\u0438 \u0438 \u0441\u0435\u043d\u0441\u043e\u0440\u043e\u043c 16K DPI."
    },
    {
        "id": "i1j9k0l23a4b5678ij90kl12mn34op56",
        "name": "\u041c\u0435\u0445\u0430\u043d\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043a\u043b\u0430\u0432\u0438\u0430\u0442\u0443\u0440\u0430 MechaKey RGB",
        "price": 6990,
        "description": "\u041a\u043b\u0430\u0432\u0438\u0430\u0442\u0443\u0440\u0430 \u0441 \u043c\u0435\u0445\u0430\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u043c\u0438 \u043f\u0435\u0440\u0435\u043a\u043b\u044e\u0447\u0430\u0442\u0435\u043b\u044f\u043c\u0438, RGB-\u043f\u043e\u0434\u0441\u0432\u0435\u0442\u043a\u043e\u0439 \u0438 \u0443\u0434\u043e\u0431\u043d\u043e\u0439 \u044d\u0440\u0433\u043e\u043d\u043e\u043c\u0438\u043a\u043e\u0439."
    },
    {
        "id": "j2k0l1m34a5b6789jk01lm23no45pq67",
        "name": "\u041c\u043e\u043d\u0438\u0442\u043e\u0440 UltraView 27",
        "price": 25990,
        "description": "27-\u0434\u044e\u0439\u043c\u043e\u0432\u044b\u0439 144 \u0413\u0446 \u043c\u043e\u043d\u0438\u0442\u043e\u0440 \u0441 IPS-\u043c\u0430\u0442\u0440\u0438\u0446\u0435\u0439 \u0438 \u0440\u0430\u0437\u0440\u0435\u0448\u0435\u043d\u0438\u0435\u043c 2K."
    },
    {
        "id": "k3l1m2n45a6b7890kl12mn34op56qr78",
        "name": "\u0412\u043d\u0435\u0448\u043d\u0438\u0439 SSD DiskFast 1TB",
        "price": 12990,
        "description": "\u0412\u044b\u0441\u043e\u043a\u043e\u0441\u043a\u043e\u0440\u043e\u0441\u0442\u043d\u043e\u0439 SSD \u0441 USB-C \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441\u043e\u043c \u0438 \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c\u044e \u0447\u0442\u0435\u043d\u0438\u044f \u0434\u043e 1050 \u041c\u0411/\u0441."
    },
    {
        "id": "l4m2n3o56a7b8901lm23no45pq67rs89",
        "name": "\u0413\u0435\u0439\u043c\u043f\u0430\u0434 GameMaster Elite",
        "price": 4990,
        "description": "\u0411\u0435\u0441\u043f\u0440\u043e\u0432\u043e\u0434\u043d\u043e\u0439 \u0433\u0435\u0439\u043c\u043f\u0430\u0434 \u0441 \u0432\u0438\u0431\u0440\u043e\u043e\u0442\u0434\u0430\u0447\u0435\u0439 \u0438 \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u043e\u0439 \u041f\u041a, \u043a\u043e\u043d\u0441\u043e\u043b\u0435\u0439 \u0438 \u0441\u043c\u0430\u0440\u0442\u0444\u043e\u043d\u043e\u0432."
    },
    {
        "id": "m5n3o4p67a8b9012mn34op56qr78st90",
        "name": "\u042d\u043a\u0448\u043d-\u043a\u0430\u043c\u0435\u0440\u0430 AdventureCam 4K",
        "price": 19990,
        "description": "\u041a\u0430\u043c\u0435\u0440\u0430 \u0434\u043b\u044f \u044d\u043a\u0441\u0442\u0440\u0435\u043c\u0430\u043b\u044c\u043d\u044b\u0445 \u0443\u0441\u043b\u043e\u0432\u0438\u0439 \u0441 4K-\u0432\u0438\u0434\u0435\u043e\u0437\u0430\u043f\u0438\u0441\u044c\u044e \u0438 \u0441\u0442\u0430\u0431\u0438\u043b\u0438\u0437\u0430\u0446\u0438\u0435\u0439 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f."
    },
    {
        "id": "n6o4p5q78a9b0123no45pq67rs89tu01",
        "name": "\u0420\u043e\u0431\u043e\u0442-\u043f\u044b\u043b\u0435\u0441\u043e\u0441 CleanBot 3000",
        "price": 25990,
        "description": "\u0418\u043d\u0442\u0435\u043b\u043b\u0435\u043a\u0442\u0443\u0430\u043b\u044c\u043d\u044b\u0439 \u0440\u043e\u0431\u043e\u0442-\u043f\u044b\u043b\u0435\u0441\u043e\u0441 \u0441 \u043b\u0430\u0437\u0435\u0440\u043d\u043e\u0439 \u043d\u0430\u0432\u0438\u0433\u0430\u0446\u0438\u0435\u0439 \u0438 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0439 \u043f\u043e\u0434\u0437\u0430\u0440\u044f\u0434\u043a\u043e\u0439."
    },
    {
        "id": "o7p5q6r89a0b1234op56qr78st90uv12",
        "name": "\u042d\u043b\u0435\u043a\u0442\u0440\u043e\u0441\u0430\u043c\u043e\u043a\u0430\u0442 SpeedRide X",
        "price": 45990,
        "description": "\u0421\u043a\u043b\u0430\u0434\u043d\u043e\u0439 \u044d\u043b\u0435\u043a\u0442\u0440\u043e\u0441\u0430\u043c\u043e\u043a\u0430\u0442 \u0441 \u0437\u0430\u043f\u0430\u0441\u043e\u043c \u0445\u043e\u0434\u0430 40 \u043a\u043c \u0438 \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u044c\u044e \u0434\u043e 30 \u043a\u043c/\u0447."
    },
    {
        "id": "8b03e13a087540959c3bdf5c1bcef388",
        "name": "new item from api",
        "description": "item description",
        "price": 1231231231
    }

]


# Типы GraphQL
@strawberry.type
class CardG:
    id: str
    name: str
    description: str
    price: int


@strawberry.type
class QuestionsQuery:
    @strawberry.field(graphql_type=Optional[CardG])
    async def card(self, card_id: str):
        if el := get_card_from_db(card_id):
            return CardG(**el)
        return None

    # Получение всех вопросов
    @strawberry.field(graphql_type=list[CardG])
    async def cards(self):
        return [CardG(**el) for el in database]


schema = strawberry.Schema(query=QuestionsQuery)
graphql_app = GraphQLRouter(schema)
