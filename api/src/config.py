import os

from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())


HEADERS = {
    "accept": "*/*",
    "content-type": "application/json",
    "origin": "https://www.tinkoff.ru",
    "referer": "https://www.tinkoff.ru",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

BODY_EXAMPLE = {
    "bounds": {
        "bottomLeft": {
            "lat": 55.66440613833879,
            "lng": 37.275181970947216},
        "topRight": {
            "lat": 55.850647648064765,
            "lng": 38.05315133129878}
    },
    "filters": {
        "banks": ["tcs"],
        "showUnavailable": False,
        "currencies": ["USD"]
    },
    "zoom": 11
}

BANK_TO_BANK_ID = {
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


API_FOR_ATM = os.getenv("API_FOR_ATM", "https://api.tinkoff.ru/geo/withdraw/clusters")
POSITION_STACK_TOKEN = os.getenv("POSITION_STACK_TOKEN")

DB_HOST = os.getenv("DB_HOST", "DB_HOST")
DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
