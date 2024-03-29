from abc import ABC

import aiohttp

from config import settings


class APIInterfaceError(Exception):
    pass


class BaseAPIInterface(ABC):

    async def get_response(self, message: str, chat_id: int) -> str:
        pass


class InterpretationsInterface(BaseAPIInterface):

    def __init__(self, url: str):
        self._url = url

    async def get_response(self, message: str, chat_id: int) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.post(self._url, params={"message": message, "chat_name": str(chat_id)}) as response:
                if response.status == 200:
                    return await response.text()
                raise APIInterfaceError(f"Произошла ошибка при обращении к API. Статус код: {response.status}")


# interface have to implement get_response async method! and return response message string

api_interface = InterpretationsInterface(url=settings.API_URL)
