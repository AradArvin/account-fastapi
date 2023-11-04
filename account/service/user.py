from passlib.context import CryptContext
from bson.objectid import ObjectId

from db.db import get_collection
from exception.exception import *



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


