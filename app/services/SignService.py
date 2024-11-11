import requests
import json
from tkinter import messagebox
from dto.Sign import SignDto
class SignService():
    def __init__(self):
        self.Base_Url = "http://127.0.0.1:8000/"
    
    def CreateSign(self, sign: SignDto):
        try:
            endpoint = self.Base_Url + 'signs/create'
            print(endpoint)
            response = requests.post(endpoint, json=sign.dict())
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Sign data Not created: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def EditSign(self, sign: SignDto, id: int):
        endpoint = self.Base_Url + f'signs/edit/{id}'
        print(endpoint)
        try:
            response = requests.put(endpoint, json=sign.dict())
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Failed to edit sign: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")


    def SearchById(self, id):
        endpoint = self.Base_Url + f'signs/{id}'
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Sign Not Found: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def Delete(self, id):
        endpoint = self.Base_Url + f'signs/delete/{id}'
        try:
            response = requests.delete(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Sign Not Deleted: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def GetSigns(self):
        endpoint = self.Base_Url + 'signs'
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Failed to retrieve signs: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")