from aiogram.filters import BaseFilter
from aiogram.types import Message


class BackMenuFilter(BaseFilter):

    async def __call__(self, message: Message) -> bool:
        return message.text == "Вернуться в главное меню 🔄" or message.text == "Вернуться в главное меню"
