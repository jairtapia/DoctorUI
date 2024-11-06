from dto.Patient import PatientDto
from services.PatientsService import PatientsService

class PatientController():
    def __init__(self) -> None:
        self.Myservice = PatientsService()

    def getPatients(self):
        return self.Myservice.GetPatients()

    def Delete(self, Id: int):
        return self.Myservice.Delete(Id)

    def findById(self, Id: int):
        return self.Myservice.SearchById(Id)

    def findByName(self, Name: str):
        return self.Myservice.SearchByName(Name)

    def EditPatient(self, patient: PatientDto, id: int):
        return self.Myservice.EditPatient(patient, id)

    def CreatePatient(self, patient: PatientDto):
        return self.Myservice.CreatePatient(patient)
