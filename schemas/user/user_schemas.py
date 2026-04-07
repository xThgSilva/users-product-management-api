from pydantic import BaseModel, EmailStr

class UserRequest(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

class UserResponseBase(BaseModel):
    message: str
    user: UserResponse
