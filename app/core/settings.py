from typing import List

from pydantic.v1 import BaseSettings, validator

class Settings(BaseSettings):
    # 專案設定
    APP_TITLE: str
    APP_DESCRIPTION: str
    APP_VERSION: str
    APP_PREFIX: str
    # 伺服器設定
    SERVER_HOST: str
    SERVER_PORT: int
    SERVER_RELOAD: bool
    SERVER_UVICORN_WORKERS: int
    SERVER_UVICORN_TIMEOUT_KEEP_ALIVE: int
    # CORS 設定
    CORS_ORIGINS: List[str]
    CORS_METHODS: List[str]
    CORS_HEADERS: List[str]
    CORS_ALLOW_CREDENTIALS: bool
    CORS_MAX_AGE: int

    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    @validator('CORS_ORIGINS', 'CORS_METHODS', 'CORS_HEADERS', pre=True)
    def split_str_to_list(self, v):
        if isinstance(v, str):
            return [s.strip() for s in v.split(',') if s.strip()]
        return v

    # 作為 Pydantic 的配置資訊
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Pydantic BaseSettings 會依照以下順序自動尋找每個屬性的值
settings = Settings() # type: ignore
