from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from app.api.routes import router
from app.database import connect_to_mongo, close_mongo_connection

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
