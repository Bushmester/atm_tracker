from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.kbd import Button

from states import MainSG


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
    print(f'City: {message.text}')
    await dialog_manager.start(MainSG.currencies, mode=StartMode.NEW_STACK)
    await MainSG.currencies.set()


async def process_currencies(c: CallbackQuery, button: Button, dialog_manager: DialogManager):
    _ = c, button
    print(f'Currency: {dialog_manager.data["aiogd_context"].widget_data["currencies"]}')
    await dialog_manager.mark_closed()
    await dialog_manager.start(MainSG.banks, mode=StartMode.NEW_STACK)
    await MainSG.banks.set()


async def process_banks(c: CallbackQuery, button: Button, dialog_manager: DialogManager):
    _ = c, button
    print(f'Banks: {dialog_manager.data["aiogd_context"].widget_data["banks"]}')
    await dialog_manager.mark_closed()
    await c.message.answer('Here is the list of available ATMs:')
    await c.message.answer('If a ATM appears: you\'ll receive update message.')
    await MainSG.polling.set()


def register_handlers(dp):
    dp.register_message_handler(cmd_help, commands=['help'], state='*')
    dp.register_message_handler(cmd_settings, commands=['start', 'settings'], state='*')
    dp.register_message_handler(process_city, state=MainSG.city)
