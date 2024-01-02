import asyncio

from aiogram import Router, types, Bot
from core.middlewares.outer_middlewares import MessageTypesMW
from core.api_interfaces import api_interface
from core.text_handlers import text_handler
from core.utils import send_action


message_router = Router()
message_router.message.outer_middleware(MessageTypesMW())


@message_router.message()
async def handle_message(message: types.Message, bot: Bot):

    stop = asyncio.Event()

    task = asyncio.create_task(
        send_action(
            bot=bot,
            chat_id=message.chat.id,
            stop=stop
        )
    )
    full_response = await api_interface.get_response(
        message=message.text,
        chat_id=message.chat.id
    )

    response_chunks = text_handler(full_response)

    for chunk in response_chunks:
        await message.answer(chunk)
    stop.set()

