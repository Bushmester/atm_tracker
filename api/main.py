import asyncio
import json

import aiohttp
from fastapi import FastAPI

from constants import headers, body

app = FastAPI()


@app.get("/")
async def root():
    response = None
    async with aiohttp.ClientSession() as session:
        async with session.post(
                "https://api.tinkoff.ru/geo/withdraw/clusters",
                headers=headers,
                data=json.dumps(body)
        ) as r:
            response = await r.json()
    return response
