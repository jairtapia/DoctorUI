from dto.User import UserDto,authenticationDto
from services.UserServices import UserService

class UserController():
    def __init__(self) -> None:
        self.Myservice = UserService()

    def RegisterUser(self,auth:authenticationDto, user:UserDto):
        self.Myservice.CreateUser(auth,user)