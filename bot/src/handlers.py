import websockets
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button

from states import MainSG
from db_utils import add_client_city_by_user_id, add_client_currency_by_user_id, add_client_banks_by_user_id


async def cmd_help(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        '/help - This text.\n'
        '/settings - Configure settings.'
    )


async def cmd_settings(message: types.Message):
    await message.answer('Please, enter your city:')
    await MainSG.city.set()


async def process_city(message: types.Message, dialog_manager: DialogManager):
    city = message.text
    add_client_city_by_user_id(city, message.from_user['id'])
    await dialog_manager.start(MainSG.currencies, mode=StartMode.NEW_STACK)
    await MainSG.currencies.set()


async def process_currencies(c: CallbackQuery, button: Button, dialog_manager: DialogManager):
    _ = button
    currency = dialog_manager.data["aiogd_context"].widget_data["currency"]
    add_client_currency_by_user_id(currency, c.from_user['id'])
    await dialog_manager.mark_closed()
    await dialog_manager.start(MainSG.banks, mode=StartMode.NEW_STACK)
    await MainSG.banks.set()


async def process_banks(c: CallbackQuery, button: Button, dialog_manager: DialogManager):
    _ = button
    banks = dialog_manager.data["aiogd_context"].widget_data["banks"]
    add_client_banks_by_user_id(banks, c.from_user['id'])
    await dialog_manager.mark_closed()
    await c.message.answer('Here is the list of available ATMs:')
    await c.message.answer('If a ATM appears: you\'ll receive update message.')
    await MainSG.polling.set()
    await process_polling(c.message)


async def process_polling(message: types.Message):
    async with websockets.connect('ws://localhost:8000/ws/{client}') as ws:
        data = await ws.recv()
    await message.answer(str(data))


def register_handlers(dp):
    dp.register_message_handler(cmd_help, commands=['help'], state='*')
    dp.register_message_handler(cmd_settings, commands=['start', 'settings'], state='*')
    dp.register_message_handler(process_city, state=MainSG.city)
