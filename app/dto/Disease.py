from pydantic import BaseModel
from typing import Optional

class DiseaseDto(BaseModel):
    id: Optional[int] = None
    name: str
    peligro:int

    class Config:
        orm_mode = True

