import os

from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters.state import StatesGroup, State
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())


API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


class MainSG(StatesGroup):
    city = State()
    currencies = State()
    banks = State()


if __name__ == '__main__':
    executor.start_polling(dp)
