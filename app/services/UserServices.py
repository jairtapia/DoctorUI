from dto.User import UserDto,authenticationDto
import requests
import json

class UserService():
    def __init__(self):
        self.Base_Url = "http://127.0.0.1:8000/"
    
    def CreateUser(self,user:UserDto):
        try:
            endpoint = self.Base_Url+'Signin/data'
            response = requests.post(endpoint,json=user.dict())
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            return f"Error al crear usuario: {e}"
        

    def CreateCrd(self,crd:authenticationDto):
        try:
            endpoint = self.Base_Url + 'Signin'
            response = requests.post(endpoint,json=crd.dict())
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            return f"Error al crear credenciales: {e}"

    def EditUser(self):
        pass

    def SearchByname(self,name):
        endpoint = self.Base_Url + f'User/find/name/fname?name={name}'
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            return f"Error al crear credenciales: {e}"

    def searchByid(self,id):
        endpoint = self.Base_Url + f'User/find/user_id?id={id}'
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
                return f"Error al crear credenciales: {e}"

    def Delete(self,id):
        endpoint = self.Base_Url + f'User/delete/user_id?id={id}'
        try:
            response = requests.delete(endpoint)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            return f"Error al crear credenciales: {e}"

    def GetUsers(self):
        endpoint = self.Base_Url + 'users'
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            return f"Error al crear credenciales: {e}"


class AuthService():
    def __init__(self):
        self.Base_Url = "http://127.0.0.1:8000/"

    def log_in(self,Auth:authenticationDto):
        endpoint = self.Base_Url+'Login'
        print(Auth)
        try:
            response = requests.post(endpoint,json=Auth.dict())
            if response.status_code == 200:
                user = response.json()
                return user
            else:
                return response.json()
        except Exception as e:
            return f"Error credenciales invalidas: {e}"
        

    def sign_in(self,Auth:authenticationDto, User:UserDto):
        storageService = UserService()
        try:
            print(storageService.CreateCrd(Auth))
            print(storageService.CreateUser(User))
            return "Usuario creado exitosamente"
        except Exception as e:
            return f"Error al crear usuario: {e}"