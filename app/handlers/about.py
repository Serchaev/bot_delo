from aiogram import F, Router
from aiogram.enums import parse_mode, ParseMode
from aiogram.types import Message

from app.filters.chat_type import ChatTypeFilter
from app.keyboards.keyboard_consultation import keyboard as keyboard_consultation

router = Router()


@router.message(
    ChatTypeFilter(chat_type="private"),
    F.text == "О Компании",
)
async def about(message: Message):
    await message.answer(
        text="<b>Воплотим ваши самые смелые идеи и желания в интерьере!</b>\n\n"
        "Мы не просто делаем ремонт — мы создаем идеальное пространство для жизни, "
        "сочетая красоту и функциональность. Более 12 лет мы приносим в дома счастье и уют.\n\n"
        "🎬 Переходите по ссылке, чтобы познакомиться с нашими работами и узнайте, "
        "как может выглядеть интерьер вашего дома."
        " → https://t.me/instroy61",
        reply_markup=keyboard_consultation,
        parse_mode=ParseMode.HTML,
    )
