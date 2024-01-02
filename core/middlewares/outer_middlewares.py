from typing import Callable, Dict, Any, Awaitable

from aiogram.types import Message
from aiogram import BaseMiddleware


class MessageTypesMW(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        if not event.text:
            await event.delete()
            await event.answer("Сообщение должно быть текстом.")
        else:
            return await handler(event, data)
