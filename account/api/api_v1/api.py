from fastapi import APIRouter, Body, status, HTTPException, Depends
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId

from schema.user import *
from service.user import *
from connection.httpx_manager import httpx_response


account_router = APIRouter()
data_router = APIRouter()

user_collection = get_collection()



@account_router.post(path="/api/v1/signup", summary="User Signup", response_model=Tokens, status_code=status.HTTP_201_CREATED)
async def user_signup(user: User = Body(), 
                      user_service: UserService = Depends(),):
    
    user = jsonable_encoder(user)

    if await user_collection.find_data_by_another_field(field_name="email", field_data=user["email"]):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User with this email already exists!")
    
    created_user = await user_service.add_user(user)

    user_id = {"id":str(created_user.inserted_id)}
    response_data = await httpx_response("api/v1/signup", user_id)

    return response_data




@account_router.post(path="/api/v1/login", summary="User Login", response_model=Tokens, status_code=status.HTTP_200_OK)
async def user_login(login_data: UserLogin = Body(), 
                     user_service: UserService = Depends(),):
    
    login_data = jsonable_encoder(login_data)

    try: 
        user = await user_service.authenticate(email=login_data["email"], password=login_data["password"])
    except UserNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Error. Please check your entered email/password.")

    response_data = await httpx_response("api/v1/login", user)

    return response_data




