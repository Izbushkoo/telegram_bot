from typing import Optional

import sqlalchemy
import sqlmodel
from pydantic import config
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int = Field(default=None, sa_type=sqlmodel.BigInteger, primary_key=True)
    first_name: Optional[str]
    last_name: Optional[str]
    username: Optional[str]

