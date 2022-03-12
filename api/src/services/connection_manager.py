from fastapi import WebSocket

from services.singleton import Singleton
from services.subscribers import Subscribers


class ConnectionManager(metaclass=Singleton):
    async def connect(self, websocket: WebSocket):
        await websocket.accept()

    def disconnect(self, websocket: WebSocket):
        pass

    async def broadcast(self):
        pass
