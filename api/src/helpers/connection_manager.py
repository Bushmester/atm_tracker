import json

from fastapi import WebSocket

from helpers.singleton import Singleton
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
        pass


manager = ConnectionManager()
