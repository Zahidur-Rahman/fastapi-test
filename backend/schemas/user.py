from pydantic import BaseModel,EmailStr,Field


class UserCreate(BaseModel):
    email:EmailStr
    password:str=Field(...,min_length=5)




class ShowUser(BaseModel):
    id:int
    email:EmailStr
    is_active:bool

    class Config():
       from_attributes=True




