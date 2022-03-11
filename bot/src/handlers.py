from aiogram import types
from aiogram.dispatcher import FSMContext

from states import MainSG


async def cmd_help(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        '/help - This text.\n'
        '/settings - Configure settings.'
    )


async def cmd_settings(message: types.Message):
    await MainSG.city.set()
    await message.answer('Please, enter your city:')


async def process_city(message: types.Message):
    await MainSG.currencies.set()
    await message.reply(message.text)
    await message.answer('Please, select currencies:')


async def process_currencies(message: types.Message):
    await MainSG.banks.set()
    await message.reply(message.text)
    await message.answer('Please, select banks:')


async def process_banks(message: types.Message, state: FSMContext):
    await state.finish()
    await message.reply(message.text)


def register_handlers(dp):
    dp.register_message_handler(cmd_help, commands=['help'], state='*')
    dp.register_message_handler(cmd_settings, commands=['start', 'settings'], state='*')
    dp.register_message_handler(process_city, state=MainSG.city)
    dp.register_message_handler(process_currencies, state=MainSG.currencies)
    dp.register_message_handler(process_banks, state=MainSG.banks)
