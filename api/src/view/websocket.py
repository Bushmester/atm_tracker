from fastapi import WebSocket, WebSocketDisconnect, APIRouter

from helpers.connection_manager import manager


router = APIRouter(tags=["ws"])


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            manager.connect(websocket, data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
