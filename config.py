from typing import Optional, Any, Generator

from pydantic import PostgresDsn, field_validator
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):

    API_URL: str

    BOT_TOKEN: str
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: int
    SQLALCHEMY_DATABASE_URI_ASYNC: Optional[PostgresDsn] = None

    @field_validator(__field="SQLALCHEMY_DATABASE_URI_ASYNC", mode='before')
    def assemble_db_connection_async(cls, v: Optional[str], values: ValidationInfo) -> Any:
        if isinstance(v, str) and v is not None:
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=values.data.get("POSTGRES_USER"),
            password=values.data.get("POSTGRES_PASSWORD"),
            host=values.data.get("POSTGRES_SERVER") + ":" + str(values.data.get("POSTGRES_PORT")),
            path=f"{values.data.get('POSTGRES_DB') or ''}",
        )


settings = Settings()
