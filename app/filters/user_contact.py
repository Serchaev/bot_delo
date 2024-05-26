from aiogram.filters import BaseFilter
from aiogram.types import Message


class UserContactFilter(BaseFilter):

    async def __call__(self, message: Message) -> bool:
        return message.contact is not None
