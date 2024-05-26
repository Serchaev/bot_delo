from datetime import datetime

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters.command import CommandStart, CommandObject
from aiogram.utils.payload import decode_payload

from app.keyboards.keyboard_start import keyboard as keyboard_start
from app.core.settings import settings
from app.filters.chat_type import ChatTypeFilter
from app.filters.user_contact import UserContactFilter
from app.handlers.about import router as about_router
from app.handlers.contacts import router as contacts_router
from app.handlers.back_menu import router as back_menu_router
from app.handlers.consultation import router as consultation_router
from app.handlers.construction import router as construction_router

bot = Bot(
    token=settings.TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2),
)
dp = Dispatcher()
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")

dp.include_routers(back_menu_router)
dp.include_routers(consultation_router)
dp.include_routers(about_router)
dp.include_routers(contacts_router)
dp.include_routers(construction_router)


@dp.message(
    ChatTypeFilter(chat_type="private"),
    CommandStart(),
)
async def cmd_start(message: types.Message, command: CommandObject):
    try:
        payload = decode_payload(command.args)
    except:
        payload = None

    ...  # создание нового пользователя в бд
    hello_text = ...  # получение преветствия из бд

    hello_text = (
        f"Я бот Строительной компании «ИнСтрой»\.\n\n"
        f"Я помогу прикинуть стоимость дома, подробнее расскажу о компании, "
        f"свяжу со специалистом и многое другое\.\n\n"
        f"Ниже в меню выберите с чего бы вам хотелось начать\.\n\n"
        f"*⚠️ Если кнопочное меню не видно, нажмите иконку 🎛 в правом нижнем углу*"
    )
    await message.answer(
        f"Здравствуйте, {message.chat.first_name}\!\n\n{hello_text}",
        reply_markup=keyboard_start,
    )


@dp.message(UserContactFilter())
async def test(message: types.Message):
    print(message.contact)
    print(message.text)


async def main():
    while True:
        try:
            await dp.start_polling(bot)
        finally:
            print("end")
