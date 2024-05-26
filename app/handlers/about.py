from aiogram import F, Router
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
        text="По статусу на конец 2021 года мы построили более 150 домов в 5 регионах России\."
        "\n\nМы строим без экономии на материалах и качестве\. Без пустых обещаний\. Без заниженных цен\."
        "\n\nНаш девиз — открыто, честно, правильно\!"
        "\n\nПосмотрите короткое видео о нас👇"
        "\nhttps://www\.youtube\.com/watch?v\=K3W25Kz2NI8",
        reply_markup=keyboard_consultation,
    )
