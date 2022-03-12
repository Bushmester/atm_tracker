from fastapi import WebSocket

from src.main import app


@app.websocket("ws/")
async def websocket_endpoint(websocket: WebSocket):
    pass
