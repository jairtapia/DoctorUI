from dto.User import UserDto,authenticationDto
from services.UserServices import UserService

class UserController():
    def __init__(self) -> None:
        self.Myservice = UserService()

    def getUsers(self):
        return self.Myservice.GetUsers()
    
    def Delete(self,Id:int):
        return self.Myservice.Delete(Id)
