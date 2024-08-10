from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.utils.payload import encode_payload

from app.core.services.refer_service import ReferService
from app.core.settings import settings
from app.filters.chat_type import ChatTypeFilter
from app.keyboards.keyboard_only_start import keyboard as keyboard_only_start
from app.texts.ref_text import ref_text

router = Router()


@router.message(
    ChatTypeFilter(chat_type="private"),
    F.text == "Получить партнерскую ссылку 🤝",
)
async def ref_program(message: Message):
    count_added = await ReferService.get_count_children(tg_id=str(message.from_user.id))
    deeplink = f"{settings.BOT_USERNAME}?start={encode_payload(payload=str(message.from_user.id))}"
    text = (
        f"Ваша ссылка:\n\n"
        f"{deeplink}\n\n"
        f"Ваши друзья: {count_added}\n\n"
        f"<b>Вы можете использовать шаблон для отправки друзьям👇</b>"
    )
    text2 = f"{ref_text}\n{deeplink}"
    await message.bot.send_message(
        chat_id=message.chat.id,
        text=text,
        parse_mode=ParseMode.HTML,
    )
    await message.answer(
        text=text2,
        reply_markup=keyboard_only_start,
        parse_mode=ParseMode.HTML,
    )
