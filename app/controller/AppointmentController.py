from services.AppointmentServices import appointmentService
from dto.Appointments import AppointmentDto

class appointmentController():
    def __init__(self) -> None:
        self.Myservice = appointmentService()

    def getAppointmentsByDoctor(self,id:int):
        return self.Myservice.getAppointmentsByDoctor(id)

    def getAppointments(self):
        return self.Myservice.getAppointments()
    
    def getPatients(self):
        return self.Myservice.getPatients()
    
    def create(self,cita:AppointmentDto):
        return self.Myservice.CreateAppointment(cita)
    
    def findById(self,value:int):
        return self.Myservice.findById(value)
    
    def Delete(self,id:int):
        return self.Myservice.Delete(id)