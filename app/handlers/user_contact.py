from aiogram import Router, types

from app.core.services.consultation_service import ConsultationService
from app.filters.user_contact import UserContactFilter
from app.keyboards.keyboard_start import keyboard as keyboard_start

router = Router()


@router.message(UserContactFilter())
async def test(message: types.Message):
    try:
        await ConsultationService.add_consultation(
            phone_number=message.contact.phone_number,
            first_name=message.contact.first_name,
            last_name=message.contact.last_name,
            tg_id=str(message.contact.user_id),
        )
    except Exception:
        await message.answer(
            text="Произошла ошибка. Попробуйте позже.",
            reply_markup=keyboard_start,
            parse_mode=None,
        )
    else:
        await message.answer(
            text="Отлично! Ожидайте, скоро с вами свяжется специалист.",
            reply_markup=keyboard_start,
            parse_mode=None,
        )
