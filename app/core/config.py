from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Architecture Lab"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False

    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file="env/local.env",
        env_file_encoding="utf-8",
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()