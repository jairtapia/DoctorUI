from services.AppointmentServices import appointmentService


class appointmentController():
    def __init__(self) -> None:
        self.Myservice = appointmentService()

    def getAppointmentsByDoctor(self,id:int):
        return self.Myservice.getAppointmentsByDoctor(id)