from passlib.context import CryptContext
from bson.objectid import ObjectId

from db.db import get_collection
from exception.exception import *



class UserService:
    
    PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")

