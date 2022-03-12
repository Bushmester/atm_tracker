from fastapi import WebSocket, WebSocketDisconnect

from main import app, manager


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            await manager.connect(websocket, data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
