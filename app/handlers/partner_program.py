from aiogram import F, Router
from aiogram.types import Message

from app.filters.chat_type import ChatTypeFilter
from app.keyboards.keyboard_referal_program import keyboard as keyboard_referal_program
from app.texts.partner_program_text import partner_program_text

router = Router()


@router.message(
    ChatTypeFilter(chat_type="private"),
    F.text == "Партнерская программа 🤝",
)
async def partner_program(message: Message):
    await message.answer(
        text=partner_program_text,
        reply_markup=keyboard_referal_program,
        parse_mode=None,
    )
