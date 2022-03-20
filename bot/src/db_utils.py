from db import CLIENTS


def get_client_or_create_by_user_id(user_id: int) -> dict:
    try:
        client = list(filter(lambda x: x['user_id'] == user_id, CLIENTS))[0]
    except IndexError:
        client = {'user_id': user_id, 'data': {}}
        CLIENTS.append(client)
    return client


def add_client_city_by_user_id(city: str, user_id: int) -> None:
    client = get_client_or_create_by_user_id(user_id)
    client['data']['city'] = city


def add_client_currency_by_user_id(currency: str, user_id: int) -> None:
    client = get_client_or_create_by_user_id(user_id)
    client['data']['currency'] = currency


def add_client_banks_by_user_id(banks: list, user_id: int) -> None:
    client = get_client_or_create_by_user_id(user_id)
    client['data']['banks'] = banks


def get_clients(city: str = None, currency: str = None, banks: list = None, user_id: int = None) -> list:
    return list(
        filter(
            lambda x: True
            and (city is None or 'city' in x.keys() and x['city'] == city)
            and (currency is None or 'currency' in x.keys() and x['currency'] == currency)
            and (banks is None or 'banks' in x.keys() and sorted(x['banks']) == sorted(banks))
            and (user_id is None or 'user_id' in x.keys() and x['user_id'] == user_id),
            CLIENTS
        )
    )
