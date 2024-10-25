from pydantic import BaseModel,EmailStr,Field
from datetime import date
from typing import Optional

class UserDto(BaseModel):
    user_id: Optional[int] = None
    user_name: str 
    last_name_f: str 
    last_name_m: str 
    telefono: str
    user_type: int

class authenticationDto(BaseModel):
    email:EmailStr
    password:str = Field(..., min_length= 8)
