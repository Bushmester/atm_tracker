import json
from typing import List

import aiohttp

from config import HEADERS, API_FOR_ATM
from services.generate_body import generate_body


async def get_data_about_atm_from_api(city: str, currency: str, banks: List[str]):
    response = None
    body = await generate_body(city, currency, banks)
    async with aiohttp.ClientSession() as session:
        async with session.post(
                API_FOR_ATM,
                headers=HEADERS,
                data=json.dumps(body)
        ) as r:
            response = await r.json()
    return response
