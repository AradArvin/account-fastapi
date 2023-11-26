import motor.motor_asyncio
from pydantic import BaseModel
from bson.objectid import ObjectId
from core import settings


# The main class that manages the connection to mongodb.
class MongoDBConnectionManager:

    HOST_ADDRESS = settings.MONGODB_HOST_ADDRESS


    def __init__(self, database: str, collection: str) -> None:
        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.HOST_ADDRESS)
        self.database = self.client[database]
        self.collection = self.database[collection]


    async def find_data_by_id(self, instance_id: ObjectId):
        """
        Find document in collection by it's object id, and return it for further use.
        """
        result = await self.collection.find_one({"_id":instance_id})
        if result:
            result["id"] = str(result["_id"])
            del[result['_id']]
        return result


    async def find_data_by_another_field(self, field_name: str, field_data: str):
        """
        Find document in collection by any field, and return it for further use.
        """
        result = await self.collection.find_one({f"{field_name}":field_data})
        if result:
            result["id"] = str(result["_id"])
            del[result['_id']]
        return result
    

    async def save_data_to_db_collection(self, instance: BaseModel):
        """
        Insert data to MongoDB.
        """
        result = await self.collection.insert_one(instance)
        return result


    async def get_data_from_db_collection(self):
        """
        Return all the documents in a mongodb collection.
        """
        data_list = list()

        collection_data = await self.collection.find()

        for data in collection_data:
            data["id"] = str(data["_id"])
            del[data['_id']]
            data_list.append(data)

        return data_list
    

    async def get_data_by_query(self, field_name: str, value: any):
        """
        Return all the documents in a mongodb collection that match a certain criteria.
        """
        data_list = list()

        collection_data = await self.collection.find({field_name: value})

        for data in collection_data:
            data["id"] = str(data["_id"])
            del[data['_id']]
            data_list.append(data)

        return data_list
    

    async def delete_data_from_db_collection(self, instance_id: ObjectId):
        """
        Delete a document.
        """
        result = await self.collection.find_one_and_delete({"_id":instance_id})
        return result


    async def update_db_collection_data(self, instance_id: ObjectId, updated_instance: BaseModel):
        """
        Update a document.
        """
        result = await self.collection.update_one({"_id": instance_id}, {"$set": updated_instance})
        return result