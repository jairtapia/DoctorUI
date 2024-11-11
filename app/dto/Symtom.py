from pydantic import BaseModel
from typing import Optional

class SymptomDto(BaseModel):
    id: Optional[int] = None
    name: str
    descripcion:str
    
    class Config:
        orm_mode = True
