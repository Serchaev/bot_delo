from aiogram.fsm.state import State, StatesGroup


class CalculateRemont(StatesGroup):
    where_make_remont = State()
    what_remont_planning = State()
    how_square_meters = State()
    do_get_key = State()
    contacts = State()
