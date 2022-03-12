import asyncio
import functools
import json
from typing import Callable

import aiohttp
from fastapi import FastAPI

from config import HEADERS, BODY

app = FastAPI()


@app.get("/")
async def root():
    response = None
    async with aiohttp.ClientSession() as session:
        async with session.post(
                "https://api.tinkoff.ru/geo/withdraw/clusters",
                headers=HEADERS,
                data=json.dumps(BODY)
        ) as r:
            response = await r.json()
    return response
