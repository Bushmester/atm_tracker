import json

from fastapi import WebSocket

from helpers.serializer import serializer_response
from helpers.singleton import Singleton
from services.get_data import get_data_about_atm_from_api
from services.hash_data import hash_data
from services.subscribers import Subscribers


class ConnectionManager(metaclass=Singleton):
    def __init__(self):
        self.subscribers = Subscribers()

    def connect(self, websocket: WebSocket, data: json):
        city = data["city"]
        currency = data["currency"]
        banks = data["banks"]
        data_hash = hash_data(city, currency, banks)
        self.subscribers.subscribers.setdefault(data_hash, {}).setdefault("config", {})
        self.subscribers.subscribers[data_hash]["config"]["city"] = city
        self.subscribers.subscribers[data_hash]["config"]["currency"] = currency
        self.subscribers.subscribers[data_hash]["config"]["banks"] = banks
        self.subscribers.subscribers[data_hash].setdefault("clients", []).append(websocket)

    def disconnect(self, websocket: WebSocket):
        subs = self.subscribers.subscribers
        for sub in subs.copy():
            clients = subs[sub]["clients"]
            if websocket in clients:
                clients.remove(websocket)
            if not subs[sub]["clients"]:
                subs.pop(sub)

    async def broadcast(self):
        subs = self.subscribers.subscribers
        for sub in subs:
            config = subs[sub]["config"]
            clients = subs[sub]["clients"]
            response = await get_data_about_atm_from_api(config["city"], config["currency"], config["banks"])
            data = await serializer_response(response)

            data_hash = hash_data(config["city"], config["currency"], config["banks"])
            prev_data = self.subscribers.subscribers[data_hash].setdefault("data", {})

            new_atms = {}
            updated_atms = {}
            obsolete_atms = {}
            for atm in data:
                if atm in prev_data:
                    if prev_data[atm]["currencies"][config["currency"]] == data[atm]["currencies"][config["currency"]]:
                        pass
                    else:
                        updated_atms[atm] = data[atm]
                else:
                    new_atms[atm] = data[atm]

            for client in clients:
                await client.send_bytes(json.dumps(data, ensure_ascii=False).encode())


manager = ConnectionManager()
