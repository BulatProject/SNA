from enum import Enum
from functools import lru_cache

from pydantic import BaseSettings

from src.core.settings.cors import CORSSettings
from src.core.settings.database import DatabaseSettings
from src.core.settings.sqlalchemy import SqlAlchemySettings
from src.core.settings.uvicorn import UvicornSettings


class RunMode(str, Enum):
    background = "BACKGROUND"
    dev = "DEV"


class Settings(BaseSettings):
    """Deposit Service API settings."""

    class Config:
        env_file = ".env"
        env_nested_delimiter = "__"

    root_path: str = ""
    app_version: str = "latest"
    project_name: str
    secret_jwt: str
    secret_key: str
    logging_level: str

    # application run mod: DEV/BACKGROUND
    run_mode: RunMode | None = RunMode.dev

    debug: bool | None

    postgres: DatabaseSettings = DatabaseSettings()
    uvicorn: UvicornSettings = UvicornSettings()
    sqlalchemy: SqlAlchemySettings = SqlAlchemySettings()
    cors: CORSSettings = CORSSettings()


@lru_cache
def get_settings() -> Settings:
    """Gatting and cashing project's settings."""
    _settings = Settings()
    return _settings


settings = get_settings()
