from fastapi import APIRouter, Body, status, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

from schema.user import *
from service.user import *
from connection.httpx_manager import httpx_response


account_router = APIRouter()
data_router = APIRouter()

user_collection = get_collection()



