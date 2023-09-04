from pydantic import BaseModel , EmailStr

from typing import Optional

class Signup(BaseModel):
    id:Optional[int]
    username:str
    email:EmailStr
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]

    class Config:
        orm_mode = True
        schema_extra={
            "example":{
                "id":1,
                "username":"admin",
                "email":"xngaleu@gmail.com",
                "password":"123456",
                "is_staff":False,
                "is_active":True
                
        }

    }

class Login(BaseModel):
    username:str  
    password:str


class Token(BaseModel):
    access_token:str
    token_type:str


class order(BaseModel):
    id:Optional[int]
    quantity:int
    order_status:Optional[str]="PENDING"
    user_id:Optional[int]
    p_name:str

    class Config:
        orm_mode = True
        schema_extra={
            "example":{
                "id":1,
                "quantity":1,
                "order_status":"PENDING",
                "p_name":"Pizza"

            }

        }

class Menu(BaseModel):

    id:Optional[int]
    name:str
    price:float
    description:str
    category:str

    class Config:
        orm_mode = True
        schema_extra={
            "example":{
                "id":1,
                "name":"Pizza",
                "price":10,
                "description":"Pizza delicious",
                "category":"Traditional"
            }
        }