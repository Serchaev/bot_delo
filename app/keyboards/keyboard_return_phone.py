from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

buttons = [
    [
        KeyboardButton(text="📱 Отправить", request_contact=True),
    ],
    [
        KeyboardButton(text="Вернуться в главное меню 🔄"),
    ],
]
keyboard = ReplyKeyboardMarkup(
    keyboard=buttons,
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню",
)
