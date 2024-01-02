import asyncio

from aiogram import Bot


async def send_action(bot: Bot, chat_id: int, stop: asyncio.Event):

    while True:
        if not stop.is_set():
            await bot.send_chat_action(chat_id=chat_id, action="typing")
        else:
            break
        await asyncio.sleep(4)
