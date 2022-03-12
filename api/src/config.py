HEADERS = {
    'accept': '*/*',
    'content-type': 'application/json',
    'origin': 'https://www.tinkoff.ru',
    'referer': 'https://www.tinkoff.ru',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-platform': 'Windows',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

BODY = {
    'bounds': {
        'bottomLeft': {
            'lat': 55.66440613833879,
            'lng': 37.275181970947216},
        'topRight': {
            'lat': 55.850647648064765,
            'lng': 38.05315133129878}
    },
    'filters': {
        'banks': ['tcs'],
        'showUnavailable': True,
        'currencies': ['USD']
    },
    'zoom': 11
}
