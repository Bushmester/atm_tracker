from aiogram.dispatcher.filters.state import StatesGroup, State


class MainSG(StatesGroup):
    city = State()
    currencies = State()
    banks = State()
