from fastapi import WebSocket, WebSocketDisconnect, APIRouter

from helpers.connection_manager import manager


router = APIRouter(tags=["ws"])


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            await manager.connect(websocket, data)
            await manager.send_personal_data(websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
