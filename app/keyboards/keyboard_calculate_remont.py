from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

buttons_1 = [
    [
        KeyboardButton(text="Новостройка"),
        KeyboardButton(text="Вторичка"),
    ],
    [
        KeyboardButton(text="Частный дом"),
        KeyboardButton(text="Другое"),
    ],
    [
        KeyboardButton(text="Вернуться в главное меню"),
    ],
]
keyboard_1 = ReplyKeyboardMarkup(
    keyboard=buttons_1,
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню",
)

buttons_2 = [
    [
        KeyboardButton(text="Да, по дизайн проекту, хочу разработать"),
    ],
    [
        KeyboardButton(text="Да, дизайн проект уже готов, нужен расчет"),
    ],
    [
        KeyboardButton(text="Ремонт планирую без дизайн проекта"),
    ],
    [
        KeyboardButton(text="Вернуться в главное меню"),
    ],
]
keyboard_2 = ReplyKeyboardMarkup(
    keyboard=buttons_2,
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню",
)

buttons_3 = [
    [
        KeyboardButton(text="от 40 до 60 кв.м."),
        KeyboardButton(text="от 60 до 80 кв.м."),
    ],
    [
        KeyboardButton(text="от 80 до 100 кв.м."),
        KeyboardButton(text="более 100 кв.м."),
    ],
    [
        KeyboardButton(text="Вернуться в главное меню"),
    ],
]
keyboard_3 = ReplyKeyboardMarkup(
    keyboard=buttons_3,
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню",
)

buttons_4 = [
    [
        KeyboardButton(text="Да"),
        KeyboardButton(text="Нет"),
    ],
    [
        KeyboardButton(text="Вернуться в главное меню"),
    ],
]
keyboard_4 = ReplyKeyboardMarkup(
    keyboard=buttons_4,
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню",
)
