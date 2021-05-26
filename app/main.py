from fastapi import FastAPI

from app.routers import load_routers


def get_app():
    create_app = FastAPI()
    load_routers(create_app)
    return create_app


app = get_app()
