from pydantic import BaseModel, EmailStr
from typing import Optional

class UserModel(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int]

class UpdateUserModel(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    age: Optional[int]
