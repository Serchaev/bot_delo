from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.types import Message

from app.filters.chat_type import ChatTypeFilter
from app.keyboards.keyboard_consultation import keyboard as keyboard_consultation

router = Router()


@router.message(
    ChatTypeFilter(chat_type="private"),
    F.text == "Наши контакты",
)
async def contacts(message: Message):
    await message.answer(
        text="Наши контакты\n\n"
        "🌐 cайт: https://serious-business.ru (http://taplink.cc/igor_gelver)\n\n"
        "🌐Instagram:\n"
        "https://instagram.com/serious_business.ru\n\n"
        "🌐 YouTube: https://www.youtube.com/channel/UClxZartuD1guGmNyp6n6_uQ \n\n"
        "🌐 ВК: https://vk.com/ks123ru\n\n"
        "🌐 Телеграм: https://t.me/igorgelver",
        reply_markup=keyboard_consultation,
        parse_mode=ParseMode.HTML,
    )
