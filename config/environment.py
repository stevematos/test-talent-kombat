import os
from functools import lru_cache

from pydantic import BaseSettings


@lru_cache
def get_env_filename():
    runtime_env = os.getenv("ENV")
    return f".env.{runtime_env}" if runtime_env else ".env"


class EnvironmentSettings(BaseSettings):
    API_VERSION: str = ""
    APP_NAME: str = ""
    DEBUG_MODE: bool = False

    class Config:
        env_file = get_env_filename()
        env_file_encoding = "utf-8"


API_VERSION = EnvironmentSettings().API_VERSION
APP_NAME = EnvironmentSettings().APP_NAME
DEBUG_MODE = EnvironmentSettings().DEBUG_MODE
