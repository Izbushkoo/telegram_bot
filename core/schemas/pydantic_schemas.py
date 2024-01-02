from typing import Optional

from pydantic import BaseModel, Field, config
from sqlmodel import Session, select, cast, BigInteger

from core.db_models.models import User as UserModel


class User(BaseModel):

    id: int
    first_name: Optional[str] = Field(default="")
    last_name: Optional[str] = Field(default="")
    username: Optional[str] = Field(default="")

    model_config = config.ConfigDict(extra="ignore", arbitrary_types_allowed=True)

    async def save_self(self, session: Session):
        async with session as s:
            statement = select(UserModel).where(cast(UserModel.id, BigInteger) == self.id)
            result = await s.exec(statement)
            if not result.one_or_none():
                s.add(UserModel(**self.model_dump()))
                await s.commit()

