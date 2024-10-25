from dto.User import UserDto,authenticationDto
from services.UserServices import AuthService

class AuthController():
    def __init__(self) -> None:
        self.Myservice = AuthService()

    def RegisterUser(self,auth:authenticationDto, user:UserDto):
        return self.Myservice.sign_in(auth,user)
    
    def login(self,auth:authenticationDto):
        return self.Myservice.log_in(auth)