import json

from fastapi import WebSocket

from helpers.singleton import Singleton
from services.get_data import _get_data_about_atm
from services.hash_data import hash_data
from services.subscribers import Subscribers

from services.db import insert_data


class ConnectionManager(metaclass=Singleton):
    def __init__(self):
        self.subscribers = Subscribers()

    async def connect(self, websocket: WebSocket, data: json):
        city = data["city"]
        currency = data["currency"]
        banks = data["banks"]
        await insert_data(city=city, currency=currency)
        data_hash = hash_data(city, currency, banks)
        subs = self.subscribers.subscribers
        subs.setdefault(data_hash, {}).setdefault("config", {})
        subs[data_hash]["config"]["city"] = city
        subs[data_hash]["config"]["currency"] = currency
        subs[data_hash]["config"]["banks"] = banks
        subs[data_hash].setdefault("clients", []).append(websocket)

        for sub in subs.copy():
            if sub == data_hash:
                continue
            clients = subs[sub]["clients"]
            if websocket in clients:
                clients.remove(websocket)
            if not subs[sub]["clients"]:
                subs.pop(sub)

    def disconnect(self, websocket: WebSocket):
        subs = self.subscribers.subscribers
        for sub in subs.copy():
            clients = subs[sub]["clients"]
            if websocket in clients:
                clients.remove(websocket)
            if not subs[sub]["clients"]:
                subs.pop(sub)

    async def send_personal_data(self, client: WebSocket):
        subs = self.subscribers.subscribers
        for sub in subs:
            config = subs[sub]["config"]
            clients = subs[sub]["clients"]

            if client not in clients:
                continue

            data = None
            try:
                data = json.dumps(
                    subs[sub]["state"],
                    ensure_ascii=False
                ).encode()
            except KeyError:
                data = await _get_data_about_atm(subscribers=self.subscribers.subscribers, config=config)

            await client.send_bytes(data)

    async def broadcast(self):
        subs = self.subscribers.subscribers
        for sub in subs:
            config = subs[sub]["config"]
            clients = subs[sub]["clients"]

            data = await _get_data_about_atm(subscribers=self.subscribers.subscribers, config=config)

            for client in clients:
                await client.send_bytes(data)


manager = ConnectionManager()
