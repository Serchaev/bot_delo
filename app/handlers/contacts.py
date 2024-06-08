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
        text='<b>За ремонтом? Это в  "ИнСтрой"!</b>\n\n'
        "🔑 Ремонт квартир, домов и коммерческих помещений под ключ. "
        "Современный дизайн, индивидуальные проекты, профессиональная команда — и это только начало.\n\n"
        "🔗 Познакомьтесь с нашими проектами и следите за обновлениями:"
        "\n- <b>Телеграм</b> → https://t.me/instroy61"
        "\n- <b>YouTube</b> → https://www.youtube.com/@user-zw9jt7ut2g"
        "\n- <b>ВКонтакте</b> → https://vk.com/in_stroy.remont",
        reply_markup=keyboard_consultation,
        parse_mode=ParseMode.HTML,
    )
