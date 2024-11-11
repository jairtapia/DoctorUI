
from dto.Sign import SignDto
from services.SignService import SignService

class SignController():
    def __init__(self) -> None:
        self.Myservice = SignService()

    def GetSigns(self):
        return self.Myservice.GetSigns()

    def Delete(self, Id: int):
        return self.Myservice.Delete(Id)

    def findById(self, Id: int):
        return self.Myservice.SearchById(Id)

    def EditSign(self, Sign: SignDto, id: int):
        return self.Myservice.EditSign(Sign, id)

    def CreateSign(self, Sign: SignDto):
        return self.Myservice.CreateSign(Sign)