import motor.motor_asyncio
from pydantic import BaseModel
from bson.objectid import ObjectId
from core import settings


class MongoDBConnectionManager:

