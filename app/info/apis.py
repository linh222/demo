from functools import lru_cache

from fastapi.openapi.models import APIKey

from app import config
from fastapi import APIRouter, Depends, status

from app.api_key import get_api_key

router = APIRouter()


@lru_cache()
def get_settings():
    return config.Settings()


@router.get("/")
async def root(api_key: APIKey = Depends(get_api_key)):
    return {"message": "Lead Scoring Model"}


@router.get("/info")
async def info(settings: config.Settings = Depends(get_settings), api_key: APIKey = Depends(get_api_key)):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
    }


@router.get("/health", status_code=status.HTTP_200_OK,)
async def health_check(api_key: APIKey = Depends(get_api_key)):
    return {"status": "OK", "message": "I am healthy"}


def include_router(app):
    app.include_router(router)
