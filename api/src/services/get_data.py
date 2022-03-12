import json

import aiohttp

from config import HEADERS, BODY, API_FOR_ATM


async def get_data_about_atm_from_api():
    response = None
    async with aiohttp.ClientSession() as session:
        async with session.post(
                API_FOR_ATM,
                headers=HEADERS,
                data=json.dumps(BODY)
        ) as r:
            response = await r.json()
    return response
