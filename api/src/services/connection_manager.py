from fastapi import WebSocket

from src.services.singleton import Singleton


class ConnectionManager(metaclass=Singleton):
    async def connect(self, websocket: WebSocket):
        await websocket.accept()

    def disconnect(self, websocket: WebSocket):
        pass

    async def broadcast(self):
        pass
