from fastapi import APIRouter, Body, status, HTTPException, Depends, Request
from fastapi.encoders import jsonable_encoder
from bson.objectid import ObjectId
from starlette.responses import JSONResponse

from schema.user import *
from schema.interactions import *
from service.user import *
from service.interactions import InteractionsService
from service.otp import OTPService
from jwt_auth.bearer import JWTBearer
from connection.httpx_manager import (httpx_response, 
                                      httpx_response_otp, 
                                      httpx_response_with_header, 
                                      httpx_response_with_header_and_data)



account_router = APIRouter()
data_router = APIRouter()
interactions_router = APIRouter()

user_collection = get_collection()




@account_router.post(path="/api/v1/verify", summary="User Verification", response_model=Tokens, status_code=status.HTTP_200_OK)
async def user_verify(data: OTP = Body(), 
                      otp_service: OTPService = Depends(),):
    
    data = jsonable_encoder(data)
    
    user_id_from_otp = await otp_service.get_user_id_if_verify(data["otp"])

    
    if user_id_from_otp == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="OTP expired please login again to get a new one.")

    user = await user_collection.find_data_by_id(ObjectId(user_id_from_otp))

    response_data = await httpx_response("api/v1/login", user)

    return response_data




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




@account_router.post(path="/api/v1/login", summary="User Login", response_model=Tokens)
async def user_login(login_data: UserLogin = Body(), 
                     user_service: UserService = Depends(),):
    
    login_data = jsonable_encoder(login_data)

    try: 
        user = await user_service.authenticate(email=login_data["email"], password=login_data["password"])
        user != None
    except UserNotFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Error. Please check your entered email/password.")
    
    email_response = await httpx_response_otp("api/v1/email", user)
    print("email_response", email_response)
    if email_response["status"] != "200_OK":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Verify email send failure please try again!")


    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Please verify within 2min to login..."})




@account_router.post(path="/api/v1/profile", dependencies=[Depends(JWTBearer())], summary="User profile", response_model=UserProfile)
async def user_profile(request: Request):
    
    bearer = request.headers.get("Authorization")
    user = await httpx_response_with_header("api/v1/profile", bearer)

    return user



@account_router.post(path="/api/v1/update-profile", dependencies=[Depends(JWTBearer())], summary="Update User profile", response_model=UpdateProfile)
async def update_user_profile(request: Request,
                              entered_data: UpdateProfile = Body(),):
    
    entered_data = jsonable_encoder(entered_data)

    bearer = request.headers.get("Authorization")
    updated_user = await httpx_response_with_header_and_data("api/v1/update-profile", entered_data, bearer)

    return updated_user



@account_router.post(path="/api/v1/access-token", dependencies=[Depends(JWTBearer(is_refresh=True))], summary="Get access token if logged in", response_model=AccessToken)
async def get_access_token(request: Request):
    
    bearer = request.headers.get("Authorization")
    access_token = await httpx_response_with_header("api/v1/access-token", bearer)

    return access_token



@account_router.post(path="/api/v1/logout", dependencies=[Depends(JWTBearer())], summary="Logout from account")
async def logout(request: Request):
    
    bearer = request.headers.get("Authorization")
    access_token = await httpx_response_with_header("api/v1/logout", bearer)

    return access_token




@data_router.post(path="/api/v1/mongodb", summary="User data", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def user_data(data: dict):

    user = await user_collection.find_data_by_id(ObjectId(data["id"]))

    return user




@data_router.post(path="/api/v1/mongodb-update", summary="Update User data", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def update_user_data(data: dict,
                           user_service: UserService = Depends(),):

    try:
        updated_user_data = await user_service.update_user_data(data["user_data"], data["entered_data"])
        return updated_user_data
    
    except NoDataEnteredError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No changes detected!")
