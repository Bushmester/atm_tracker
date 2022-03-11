from aiogram_dialog import Window, Dialog
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.kbd import Multiselect
from aiogram_dialog.widgets.kbd import Radio
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.text import Format

from config import CURRENCIES, BANKS
from handlers import process_banks, process_currencies
from states import MainSG

main_dialog = Dialog(
    Window(
        Const('Please, select currencies:'),
        Radio(
            Format("🔘 {item}"),
            Format("⚪️ {item}"),
            id='currencies',
            item_id_getter=lambda x: x,
            items=CURRENCIES
        ),
        Button(Const('Next'), id='next', on_click=process_currencies),
        state=MainSG.currencies
    ),
    Window(
        Const('Please, select banks:'),
        Multiselect(
            Format('✓ {item}'),
            Format('{item}'),
            id='banks',
            item_id_getter=lambda x: x,
            items=BANKS,
            min_selected=1
        ),
        Button(Const('Next'), id='next', on_click=process_banks),
        state=MainSG.banks
    )
)


def register_dialogs(registry):
    registry.register(main_dialog)
