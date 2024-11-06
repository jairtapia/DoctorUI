from pydantic import BaseModel
from datetime import datetime,time
from typing import Optional

class AppointmentDto(BaseModel):
    id: Optional[int] = None
    date: datetime
    time: time 
    patient_id: int
    doctor_id: int
    clinic_room_id: int

    class Config:
        # Definir los codificadores personalizados para datetime y time
        json_encoders = {
            datetime: lambda v: v.strftime('%Y-%m-%d'),  # Convertir datetime a solo fecha: YYYY-MM-DD
            time: lambda v: v.strftime('%H:%M:%S')      # Convertir time a string: HH:MM:SS
        }