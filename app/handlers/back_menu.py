from aiogram import Router
from aiogram.types import Message
from app.keyboards.keyboard_start import keyboard as keyboard_start
from app.filters.back_menu import BackMenuFilter

from app.filters.chat_type import ChatTypeFilter

router = Router()


@router.message(
    ChatTypeFilter(chat_type="private"),
    BackMenuFilter(),
)
async def back_menu(message: Message):
    await message.answer(
        text="Выберите что Вас интересует👇\n\n"
        f"*⚠️ Если кнопочное меню не видно, нажмите иконку 🎛 в правом нижнем углу*",
        reply_markup=keyboard_start,
    )
