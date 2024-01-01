from contextlib import asynccontextmanager
import os
import logging
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from users.routes import router as users_router
from search.routes import router as search_router
from database import connect_to_mongo, close_mongo_connection
from config import config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Make the mongo connection available to the rest of the app
    await connect_to_mongo(uri=config.mongo_uri, db_name="coppice")
    yield
    # Close the mongo connection
    await close_mongo_connection()

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(users_router)
app.include_router(search_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

