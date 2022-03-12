from fastapi import WebSocket, WebSocketDisconnect

from main import app, manager


@app.websocket("ws/")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
