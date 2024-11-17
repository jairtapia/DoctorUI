from pydantic import BaseModel,Field
from datetime import date
from typing import Optional

class DiagnosticDto(BaseModel):
    id:Optional[int] = Field(default=None)
    paciente:int
    medico:int
    fecha:date
    descripcion:str
    receta:str
    enfermedad:int
    estado:int
    
    class Config:
        orm_mode = True