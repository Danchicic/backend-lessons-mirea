import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from api.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    swagger_ui_parameters={
        "displayRequestDuration": True,  # Показать длительность запросов
    }
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)


@app.get('/')
async def redirect_to_doc():
    return RedirectResponse(url="/docs")


if __name__ == '__main__':
    uvicorn.run(app, port=8080)
