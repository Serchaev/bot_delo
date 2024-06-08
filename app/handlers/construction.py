from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.types import Message

from app.filters.chat_type import ChatTypeFilter
from app.keyboards.keyboard_consultation import keyboard as keyboard_consultation
from app.texts.remont_start import remont_start

router = Router()


@router.message(
    ChatTypeFilter(chat_type="private"),
    F.text == "С чего начать ремонт",
)
async def construction(message: Message):
    await message.answer(
        text=remont_start,
        reply_markup=keyboard_consultation,
        parse_mode=ParseMode.HTML,
    )
