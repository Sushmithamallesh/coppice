from pymongo import MongoClient
import logging

logger = logging.getLogger(__name__)

class MongoDB:
    client: MongoClient = None
    db: MongoClient = None

mongo = MongoDB()

def get_db():
    return mongo.db

async def connect_to_mongo(uri: str, db_name: str):
    try:
        logger.info(f"Connecting to MongoDB at {uri}")
        mongo.client = MongoClient(uri)
        mongo.db = mongo.client[db_name]
        # Check if the connection is established by calling a command that requires a connection
        mongo.client.admin.command('ismaster')
    except Exception as e:
        mongo.client = None
        mongo.db = None
        logger.error(f"An error occurred while connecting to MongoDB: {e}")
        raise

async def close_mongo_connection():
    if mongo.client:
        mongo.client.close()
        mongo.client = None
        mongo.db = None
