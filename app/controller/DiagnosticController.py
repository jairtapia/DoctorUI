from dto.Diagnostic import DiagnosticDto
from services.DiasgnosticService import DiagnosticService

class DiagnosticController():
    def __init__(self) -> None:
        self.Myservice = DiagnosticService()

    def getDiagnostics(self):
        return self.Myservice.Getdiagnostics()

    def Delete(self, Id: int):
        return self.Myservice.Delete(Id)

    def findById(self, Id: int):
        return self.Myservice.SearchById(Id)

    def EditDiagnostic(self, Diagnostic: DiagnosticDto, id: int):
        return self.Myservice.Editdiagnostic(Diagnostic, id)

    def CreateDiagnostic(self, Diagnostic: DiagnosticDto):
        return self.Myservice.Creatediagnostic(Diagnostic)
    
    def UpdateHistorical(self,diagnostico:int,paciente:int):
        return self.Myservice.updateHitoric(diagnostico,paciente)
    
    def GetHistorical(self,id:int):
        return self.Myservice.getHistoric(id)

