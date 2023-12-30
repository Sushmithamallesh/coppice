from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from routers.routes import router
from dependencies import connect_to_mongo, close_mongo_connection

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Make the mongo connection
    await connect_to_mongo(uri=os.environ['MONGO_URI'], db_name="coppice")
    yield
    await close_mongo_connection()
    

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
