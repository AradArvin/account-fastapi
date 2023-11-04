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
    

