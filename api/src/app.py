from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

from helpers.connection_manager import manager
from view.websocket import router


app = FastAPI()
app.include_router(router)


@app.on_event("startup")
@repeat_every(seconds=60 * 5)
async def make_broadcast():
    if manager.subscribers.subscribers:
        await manager.broadcast()


@app.get("/")
async def root():
    pass
