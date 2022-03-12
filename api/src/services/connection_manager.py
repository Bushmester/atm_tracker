import json
from typing import Dict

from fastapi import WebSocket

from services.singleton import Singleton
from services.subscribers import Subscribers


class ConnectionManager(metaclass=Singleton):
    def __init__(self):
        self.subscribers = Subscribers()

    async def connect(self, websocket: WebSocket, data: json):
        data: Dict = json.load(data)
        self.subscribers.subscribers[data["city"]]["currency"].append(websocket)
        print(self.subscribers.subscribers)

    def disconnect(self, websocket: WebSocket):
        pass

    async def broadcast(self):
        pass
