from typing import Optional

from pydantic import BaseModel, Field
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import Session
from sqlmodel import select

from core.db_models.models import User as UserModel


class User(BaseModel):

    id: int
    first_name: Optional[str] = Field(default="")
    last_name: Optional[str] = Field(default="")
    username: Optional[str] = Field(default="")

    async def save_self(self, session: Session):
        async with session as s:
            statement = select(UserModel).where(UserModel.id == self.id)
            result = await s.exec(statement)
            if not result.one_or_none():
                s.add(UserModel(**self.model_dump()))
                await s.commit()

