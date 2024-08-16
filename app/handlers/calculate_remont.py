from aiogram import Bot, F, Router
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.filters.chat_type import ChatTypeFilter
from app.filters.user_contact import UserContactFilter
from app.keyboards import keyboard_return_phone, keyboard_start
from app.keyboards.keyboard_calculate_remont import keyboard_1, keyboard_2, keyboard_3, keyboard_4
from app.states.order_remont import CalculateRemont

router = Router()


@router.message(
    ChatTypeFilter(chat_type="private"),
    F.text == "Расчитать стоимость ремонта 🏡",
)
async def construction(message: Message, state: FSMContext):
    await message.answer(
        text="Где нужно сделать ремонт?",
        reply_markup=keyboard_1,
        parse_mode=ParseMode.HTML,
    )
    await state.set_state(CalculateRemont.where_make_remont)


@router.message(
    CalculateRemont.where_make_remont,
    F.text.in_(("Новостройка", "Вторичка", "Частный дом", "Другое")),
)
async def calculate_remont_1(message: Message, state: FSMContext):
    await state.update_data(**{"Где нужно сделать ремонт?": message.text.lower()})
    await message.answer(
        text="Ремонт планируете делать по дизайн проекту?",
        reply_markup=keyboard_2,
    )
    await state.set_state(CalculateRemont.what_remont_planning)


@router.message(
    CalculateRemont.what_remont_planning,
    F.text.in_(
        (
            "Да, по дизайн проекту, хочу разработать",
            "Да, дизайн проект уже готов, нужен расчет",
            "Ремонт планирую без дизайн проекта",
        )
    ),
)
async def calculate_remont_2(message: Message, state: FSMContext):
    await state.update_data(**{"Ремонт планируете делать по дизайн проекту?": message.text.lower()})
    await message.answer(
        text="Сколько квадратных метров помещение?",
        reply_markup=keyboard_3,
    )
    await state.set_state(CalculateRemont.how_square_meters)


@router.message(
    CalculateRemont.how_square_meters,
    F.text.in_(("от 40 до 60 кв.м.", "от 60 до 80 кв.м.", "от 80 до 100 кв.м.", "более 100 кв.м.")),
)
async def calculate_remont_3(message: Message, state: FSMContext):
    await state.update_data(**{"Сколько квадратных метров помещение?": message.text.lower()})
    await message.answer(
        text="Ключи получили?",
        reply_markup=keyboard_4,
    )
    await state.set_state(CalculateRemont.do_get_key)


@router.message(
    CalculateRemont.do_get_key,
    F.text.in_(("Да", "Нет")),
)
async def calculate_remont_4(message: Message, state: FSMContext):
    await state.update_data(**{"Ключи получили?": message.text.lower()})
    await message.answer(
        text="Нажмите кнопку отправить, чтобы менеджер мог связаться с вами.",
        reply_markup=keyboard_return_phone.keyboard,
        parse_mode=None,
    )
    await state.set_state(CalculateRemont.contacts)


@router.message(
    CalculateRemont.contacts,
    UserContactFilter(),
)
async def food_chosen(message: Message, state: FSMContext, bot: Bot):
    await state.update_data(
        **{"Контакт:": f"телефон: {message.contact.phone_number}, имя: {message.contact.first_name}"}
    )
    user_data = await state.get_data()
    await state.clear()
    tmp = "\n".join((f"{key} - {value}" for key, value in user_data.items()))
    try:
        await bot.send_message(chat_id="-4157112517", text=f"Новая заявка:\n{tmp}", parse_mode=None)
    except Exception as e:
        print(e)
        print("Ошибка отправки админу")
    await message.answer(
        text="Спасибо за прохождение опроса! В ближайшее время с вами свяжется специалист.",
        parse_mode=None,
        reply_markup=keyboard_start.keyboard,
    )
