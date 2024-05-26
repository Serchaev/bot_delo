from aiogram import F, Router
from aiogram.types import Message

from app.filters.chat_type import ChatTypeFilter
from app.keyboards.keyboard_consultation import keyboard as keyboard_consultation

router = Router()


@router.message(
    ChatTypeFilter(chat_type="private"),
    F.text == "С чего начать строительство",
)
async def construction(message: Message):
    await message.answer(
        text="С чего начать строительство дома?\n\n"
        "Строительство любого дома начинается с идеи и желания иметь свой дом.\n\n"
        "Всё остальное - это уже дело техники и задачи специалистов.\n\n"
        "Правильный выбор компании, которой вы доверите решать за вас огромное количество задач по проектированию"
        " и строительству вашего дома это очень важный шаг.\n\n"
        "Если ошибиться, то легко можно остаться без денег и дома, "
        "но с испорченными нервами и недоверием ко всем строителям на всю жизнь.\n\n"
        "Мы своими силами выполняем полный спектр услуг от проектирования до строительства дома «под ключ».\n\n"
        "Если желание построить дом у вас уже есть, то начните с консультации.\n\n"
        "Мы расскажем и покажем, как легко и просто вы сможете получить ваш красиво "
        "и правильно спроектированный и построенный собственный дом.",
        reply_markup=keyboard_consultation,
        parse_mode=None,
    )
