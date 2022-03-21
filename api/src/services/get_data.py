import json
from typing import List

import aiohttp

from config import HEADERS, API_FOR_ATM
from helpers.serializer import serializer_response
from services.generate_body import generate_body
from services.hash_data import hash_data


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


async def _get_data_about_atm(subscribers, config):
    response = await get_data_about_atm_from_api(config["city"], config["currency"], config["banks"])
    current_data = await serializer_response(response)
    data_hash = hash_data(config["city"], config["currency"], config["banks"])
    prev_data = subscribers[data_hash].setdefault("data", {})

    old_atms = {}
    new_atms = {}
    updated_atms = {}
    obsolete_atms = {}

    for atm in current_data:
        if atm in prev_data:
            if prev_data[atm]["currencies"][config["currency"]] == current_data[atm]["currencies"][config["currency"]]:
                old_atms[atm] = current_data[atm]
            else:
                updated_atms[atm] = current_data[atm]
        else:
            new_atms[atm] = current_data[atm]

    for atm in prev_data:
        if atm not in current_data:
            atm_data = prev_data[atm]
            atm_data["currencies"][config["currency"]] = 0
            obsolete_atms[atm] = atm_data

    subscribers[data_hash]["data"] = current_data

    return json.dumps(
        {
            'old': old_atms,
            'new': new_atms,
            'updated': updated_atms,
            'obsolete': obsolete_atms
        },
        ensure_ascii=False
    ).encode()
