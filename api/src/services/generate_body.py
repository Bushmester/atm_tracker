import json
import zlib
from typing import List

import aiohttp

from config import BODY_EXAMPLE, BANK_TO_BANK_ID, POSITION_STACK_TOKEN


async def generate_body(city: str, currency: str, banks: List[str]):
    body = BODY_EXAMPLE.copy()

    async with aiohttp.ClientSession(auto_decompress=False) as session:
        link = f"http://api.positionstack.com/v1/forward?access_key={POSITION_STACK_TOKEN}&query={city}&bbox_module=1"
        async with session.get(link) as r:
            data = json.loads(zlib.decompress(await r.read(), 16 + zlib.MAX_WBITS).decode())
    city_coords = data["data"][0]["bbox_module"][::-1]

    (
        body["bounds"]["topRight"]["lat"],
        body["bounds"]["topRight"]["lng"],
        body["bounds"]["bottomLeft"]["lat"],
        body["bounds"]["bottomLeft"]["lng"]
    ) = city_coords
    body["filters"]["currencies"] = [currency]
    body["filters"]["banks"] = [BANK_TO_BANK_ID[bank] for bank in banks]

    return body
