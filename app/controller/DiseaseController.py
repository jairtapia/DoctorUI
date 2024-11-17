from dto.Disease import DiseaseDto
from services.DiseaseService import DiseaseService
from typing import List

class DiseaseController():
    def __init__(self) -> None:
        self.Myservice = DiseaseService()

    def GetDiseases(self):
        return self.Myservice.GetDiseases()

    def Delete(self, Id: int):
        return self.Myservice.Delete(Id)

    def findById(self, Id: int):
        return self.Myservice.SearchById(Id)
    
    def findByName(self, name: str):
        return self.Myservice.searchByName(name)

    def EditDiesase(self, Disease: DiseaseDto, id: int):
        return self.Myservice.EditDisease(Disease, id)

    def CreateDisease(self, Disease: DiseaseDto):
        return self.Myservice.CreateDisease(Disease)
    
    def getDiseaseSymptoms(self, id:int):
        return self.Myservice.getSymptoms(id)

    def getDiseaseSigns(self, id:int):
        return self.Myservice.getSigns(id)
    
    def createDiseaseSymptoms(self, id:int,data:List[int]):
        return self.Myservice.CreateSymptomsList(id,data)

    def createDiseaseSigns(self, id:int,data:List[int]):
        return self.Myservice.CreateSignsList(id,data)

    def DeleteDiseaseSymptoms(self, id:int):
        return self.Myservice.DeleteSymptoms(id)

    def DeleteDiseaseSigns(self, id:int):
        return self.Myservice.DeleteSigns(id)