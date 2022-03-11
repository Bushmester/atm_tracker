import os

from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())


TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

CURRENCIES = ['RUB', 'USD', 'EUR']

BANKS = [
    'Tinkoff',
    'Sberbank',
    'VTB Bank',
    'Alfa-bank',
    'Raiffeisen Bank',
    'GazPromBank',
    'MKB',
    'Rosbank',
    'Promsvyazbank',
    'Uralsib',
    'Otkritie'
]
