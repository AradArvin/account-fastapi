import motor.motor_asyncio
from pydantic import BaseModel
from bson.objectid import ObjectId
from core import settings


class MongoDBConnectionManager:

    HOST_ADDRESS = settings.MONGODB_HOST_ADDRESS


    def __init__(self, database: str, collection: str) -> None:
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.HOST_ADDRESS)
        self.database = self.client[database]
        self.collection = self.database[collection]

