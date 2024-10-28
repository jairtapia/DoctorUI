from dto.User import UserDto,authenticationDto
from services.UserServices import UserService

class UserController():
    def __init__(self) -> None:
        self.Myservice = UserService()

    def getUsers(self):
        return self.Myservice.GetUsers()
    
    def Delete(self,Id:int):
        return self.Myservice.Delete(Id)
    
    def findById(self,Id:int):
        return self.Myservice.searchByid(Id)

    def findByName(self,Name:str):
        return self.Myservice.SearchByname(Name)