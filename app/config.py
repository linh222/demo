import os
from os.path import join, dirname

from dotenv import load_dotenv
from pydantic import BaseSettings

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("API_KEY")
API_KEY_NAME = os.environ.get("API_KEY_NAME")


class Settings(BaseSettings):
    app_name: str = "Lead Scoring API"
    admin_email: str = "hung.le@elsanow.io"


settings = Settings()
