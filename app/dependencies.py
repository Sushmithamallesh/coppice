from pymongo import MongoClient

class MongoDB:
    client: MongoClient = None
    db: MongoClient = None

mongo = MongoDB()

def get_db():
    return mongo.db

def connect_to_mongo(uri: str, db_name: str):
    mongo.client = MongoClient(uri)
    mongo.db = mongo.client[db_name]

def close_mongo_connection():
    mongo.client.close()
