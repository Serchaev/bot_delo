from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# buttons = [
#     [
#         KeyboardButton(text="Рассчитать стоимость дома 🏡"),
#     ],
#     [
#         KeyboardButton(text="Посмотреть примеры"),
#         KeyboardButton(text="С чего начать строительство"),
#     ],
#     [
#         KeyboardButton(text="О Компании"),
#         KeyboardButton(text="Наши контакты"),
#     ],
#     [
#         KeyboardButton(text='Скачать "10 ошибок при строительстве дома"'),
#     ],
#     [
#         KeyboardButton(text="Партнерская программа 🤝"),
#     ],
# ]

buttons = [
    [
        KeyboardButton(text="О Компании"),
        KeyboardButton(text="Наши контакты"),
    ],
    [
        KeyboardButton(text="С чего начать ремонт"),
    ],
    [
        KeyboardButton(text="Партнерская программа 🤝"),
    ],
]
keyboard = ReplyKeyboardMarkup(
    keyboard=buttons,
    resize_keyboard=True,
    input_field_placeholder="Выберите пункт меню",
)
