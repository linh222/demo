import sentry_sdk
from fastapi import FastAPI
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

from app.routers import load_routers
from app.config import SENTRY_DSN, ENVIRONMENT

sentry_sdk.init(dsn=SENTRY_DSN,
                environment=ENVIRONMENT)


def get_app():
    create_app = FastAPI()
    load_routers(create_app)
    return create_app


fast_api_app = get_app()

app = SentryAsgiMiddleware(fast_api_app)
