from datetime import datetime

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters.command import CommandObject, CommandStart
from aiogram.utils.payload import decode_payload

from app.core.services.user_service import UserService
from app.core.settings import settings
from app.filters.chat_type import ChatTypeFilter
from app.filters.user_contact import UserContactFilter
from app.handlers.about import router as about_router
from app.handlers.back_menu import router as back_menu_router
from app.handlers.construction import router as construction_router
from app.handlers.consultation import router as consultation_router
from app.handlers.contacts import router as contacts_router
from app.handlers.user_contact import router as user_contact_router
from app.handlers.partner_program import router as partner_program_router
from app.handlers.ref_program import router as ref_program_router
from app.handlers.calculate_remont import router as calculate_remont_router
from app.keyboards.keyboard_start import keyboard as keyboard_start
from app.texts.hello_text import hello_text

bot = Bot(
    token=settings.TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2),
)
dp = Dispatcher()
dp["started_at"] = datetime.now().strftime("%Y-%m-%d %H:%M")

dp.include_routers(calculate_remont_router)
dp.include_routers(back_menu_router)
dp.include_routers(consultation_router)
dp.include_routers(about_router)
dp.include_routers(contacts_router)
dp.include_routers(construction_router)
dp.include_routers(user_contact_router)
dp.include_routers(partner_program_router)
dp.include_routers(ref_program_router)


@dp.message(
    ChatTypeFilter(chat_type="private"),
    CommandStart(),
)
async def cmd_start(message: types.Message, command: CommandObject):
    try:
        payload = decode_payload(command.args)
    except Exception:
        payload = None

    await UserService.add_user(
        tg_id=str(message.from_user.id),
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        refer_id=payload,
    )

    await message.answer(
        text=f"Здравствуйте, {message.chat.first_name}!\n\n{hello_text}",
        reply_markup=keyboard_start,
        parse_mode=ParseMode.HTML,
    )


async def main():
    await dp.start_polling(bot)
