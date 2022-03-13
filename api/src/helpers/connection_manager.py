import json

from fastapi import WebSocket

from helpers.singleton import Singleton
from services.subscribers import Subscribers


class ConnectionManager(metaclass=Singleton):
    def __init__(self):
        self.subscribers = Subscribers()

    def connect(self, websocket: WebSocket, data: json):
        pass

    def disconnect(self, websocket: WebSocket):
        pass

    async def broadcast(self):
        pass


manager = ConnectionManager()
