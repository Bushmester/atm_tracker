from fastapi import FastAPI

from services.connection_manager import ConnectionManager

app = FastAPI()
manager = ConnectionManager()


@app.get("/")
async def root():
    pass
