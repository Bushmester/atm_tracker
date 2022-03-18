from fastapi import FastAPI

from view.websocket import router


app = FastAPI()
app.include_router(router)


@app.get("/")
async def root():
    pass
