import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())


API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')


bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class MainSG(StatesGroup):
    city = State()
    currencies = State()
    banks = State()


@dp.message_handler(commands=['help'], state='*')
async def cmd_help(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        '/help - This text.\n'
        '/settings - Configure settings.'
    )


@dp.message_handler(commands=['start', 'settings'], state='*')
async def cmd_settings(message: types.Message):
    await MainSG.city.set()
    await message.answer('Please, enter your city:')


@dp.message_handler(state=MainSG.city)
async def process_city(message: types.Message):
    await MainSG.currencies.set()
    await message.reply(message.text)
    await message.answer('Please, select currencies:')


@dp.message_handler(state=MainSG.currencies)
async def process_currencies(message: types.Message):
    await MainSG.banks.set()
    await message.reply(message.text)
    await message.answer('Please, select banks:')


@dp.message_handler(state=MainSG.banks)
async def process_banks(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
