from pydantic import BaseModel,EmailStr,Field
from datetime import date
from typing import Optional

class PatientDto(BaseModel):
    patient_id: Optional[int] = None
    name: str
    last_name_f: str
    last_name_m: str
    age: int
    phone: str
    address: str
    state: str
