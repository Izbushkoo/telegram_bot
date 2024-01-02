from aiogram import Router, types
from core.middlewares.outer_middlewares import MessageTypesMW
from core.api_interfaces import api_interface


message_router = Router()
message_router.message.outer_middleware(MessageTypesMW())


@message_router.message()
async def handle_message(message: types.Message):

    full_response = await api_interface.get_response(message.text)
    await message.answer(full_response)
    # response_chunks = response_handler.handle_response(full_response)

    # for chunk in response_chunks:
    #     await message.answer(chunk)

