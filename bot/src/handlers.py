import json

import websockets
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button

from states import MainSG
from db_utils import (
    add_client_city_by_user_id, add_client_currency_by_user_id, add_client_banks_by_user_id,
    get_clients,
)
from utils import concatenate_dicts


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
    await MainSG.polling.set()
    await process_polling(c)


async def process_polling(c: CallbackQuery):
    client = get_clients(user_id=c.from_user['id'])[0]
    currency = client['data']['currency']

    async with websockets.connect('ws://localhost:8000/ws') as ws:
        # First message
        await ws.send(json.dumps(client['data']))
        data = json.loads(await ws.recv())

        if data:
            await c.message.answer('List of available ATMs:')
            for atm, atm_info in concatenate_dicts(
                    data['old'],
                    data['new'],
                    data['updated'],
                    data['obsolete']
            ).items():
                amount = atm_info['currencies'][currency]
                await c.message.answer(f'<b>{atm}</b>\n<i>{currency}</i>: {amount}', parse_mode=types.ParseMode.HTML)
        else:
            await c.message.answer('No available ATMs at the moment.')

        await c.message.answer('If something changes, you\'ll receive an update message.')

        # Waiting for updates
        while True:
            try:
                data = json.loads(await ws.recv())

                new_atms = data['new']
                if new_atms:
                    await c.message.answer('List of NEW ATMs:')
                    for atm, atm_info in new_atms.items():
                        amount = atm_info['currencies'][currency]
                        await c.message.answer(
                            f'<b>{atm}</b>\n<i>{currency}</i>: {amount}',
                            parse_mode=types.ParseMode.HTML
                        )

                updated_atms = data['updated']
                if updated_atms:
                    await c.message.answer('List of UPDATED ATMs:')
                    for atm, atm_info in updated_atms.items():
                        amount = atm_info['currencies'][currency]
                        await c.message.answer(
                            f'<b>{atm}</b>\n<i>{currency}</i>: {amount}',
                            parse_mode=types.ParseMode.HTML
                        )

                obsolete_atms = data['obsolete']
                if obsolete_atms:
                    await c.message.answer('List of OBSOLETE ATMs:')
                    for atm, atm_info in obsolete_atms.items():
                        amount = atm_info['currencies'][currency]
                        await c.message.answer(
                            f'<b>{atm}</b>\n<i>{currency}</i>: {amount}',
                            parse_mode=types.ParseMode.HTML
                        )

            except websockets.ConnectionClosed:
                print('Connection with server closed')
                break


def register_handlers(dp):
    dp.register_message_handler(cmd_help, commands=['help'], state='*')
    dp.register_message_handler(cmd_settings, commands=['start', 'settings'], state='*')
    dp.register_message_handler(process_city, state=MainSG.city)
