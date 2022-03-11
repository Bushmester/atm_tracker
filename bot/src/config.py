import os

from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())


TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

CURRENCIES = ['RUB', 'USD', 'EUR']

BANKS = {
    'Tinkoff': 'tcs',
    'Sberbank': '11242',
    'VTB Bank': '11249',
    'Alfa-bank': '11250',
    'Raiffeisen Bank': '11241',
    'GazPromBank': '11371',
    'MKB': '11475',
    'Rosbank': '11248',
    'Promsvyazbank': '11243',
    'Uralsib': '11245',
    'Otkritie': '11633'
}
