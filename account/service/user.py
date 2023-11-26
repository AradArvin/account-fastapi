from passlib.context import CryptContext
from bson.objectid import ObjectId

from db.db import get_collection
from exception.exception import *


# Service for user data handling.
class UserService:
    
    PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __init__(self) -> None:
        self.collection = get_collection()

    
    async def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.PWD_CONTEXT.verify(plain_password, hashed_password)


    async def get_password_hash(self, password: str) -> str:
        return self.PWD_CONTEXT.hash(password)
    

    async def get_user(self, email: str, password: str) -> dict:
        user = await self.collection.find_data_by_another_field(field_name="email", field_data=email)

        try:
            user != None
            await self.verify_password(password, user["password"])
            return user
        except:
            raise UserNotFoundError

        

    async def authenticate(self, email: str, password: str) -> dict:
        user = await self.get_user(email, password)
        return user
    


    async def add_user(self, user) -> dict:
        user["password"] = await self.get_password_hash(user["password"])
        created_user = await self.collection.save_data_to_db_collection(user)
        return created_user


    async def update_user_data(self, user_data, entered_data):

        new_user_data = {k: v for k, v in dict(entered_data).items() if v if not None}

        if len(new_user_data) >= 1:
            result = await self.collection.update_db_collection_data(instance_id=ObjectId(user_data["id"]), updated_instance=new_user_data)
        else:
            result = None 
        
        try:
            result != None
        except:
            raise NoDataEnteredError

        updated_user_data = await self.collection.find_data_by_id(instance_id=ObjectId(user_data["id"]))
        return updated_user_data