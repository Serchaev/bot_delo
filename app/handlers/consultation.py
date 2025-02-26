from aiogram import F, Router
from aiogram.types import Message

from app.filters.chat_type import ChatTypeFilter
from app.keyboards.keyboard_return_phone import keyboard as keyboard_return_phone

router = Router()


@router.message(
    ChatTypeFilter(chat_type="private"),
    F.text == "Консультация",
)
async def consultation(message: Message):
    await message.answer(
        text="Отправьте свой контакт, чтобы менеджер мог связаться с вами.",
        reply_markup=keyboard_return_phone,
        parse_mode=None,
    )
