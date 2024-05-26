from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

buttons = [
    [
        KeyboardButton(text="Консультация"),
    ],
    [
        KeyboardButton(text="Вернуться в главное меню"),
    ],
]
keyboard = ReplyKeyboardMarkup(
    keyboard=buttons,
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню",
)
