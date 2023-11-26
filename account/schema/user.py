from pydantic import BaseModel, Field, EmailStr


# Schemas for mongodb document design and a way to know the data structure for each document.

class User(BaseModel):
    _id: str
    username: str | None=None
    fullname: str | None=None
    email: EmailStr = Field()
    password: str = Field()

    class Config:
        populate_by_name = True


class UserResponse(BaseModel):
    id: str
    username: str | None=None
    fullname: str | None=None
    email: EmailStr = Field()
    password: str = Field()


class UserProfile(BaseModel):
    username: str | None=None
    fullname: str | None=None
    email: EmailStr = Field()



class UpdateProfile(BaseModel):
    username: str | None=None
    fullname: str | None=None
    email: EmailStr | None=None


class UserLogin(BaseModel):
    _id: str
    email: EmailStr = Field()
    password: str = Field()




class Tokens(BaseModel):
    access: str = Field()
    refresh: str = Field()



class AccessToken(BaseModel):
    access: str = Field()



class OTP(BaseModel):
    otp: str = Field()