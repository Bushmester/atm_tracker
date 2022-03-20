import time

from fastapi import WebSocket, WebSocketDisconnect, APIRouter

from helpers.connection_manager import manager


router = APIRouter(tags=["ws"])


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        is_first = True
        while True:
            if is_first:
                data = await websocket.receive_json()
                manager.connect(websocket, data)
                await manager.broadcast()
                is_first = False
            time.sleep(60)
            await manager.broadcast()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
