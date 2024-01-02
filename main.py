import logging
import asyncio
import os
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from core.routers.messages_router import message_router
from core.schemas.pydantic_schemas import User
from core.database import session_maker
from config import settings


dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message) -> None:
    user = User(
        **message.from_user.model_dump()
    )
    await user.save_self(session_maker())

    await message.answer("Done")


async def main() -> None:

    bot = Bot(token=settings.BOT_TOKEN)
    dp.include_router(message_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
