import requests
import json
from tkinter import messagebox
from dto.Disease import DiseaseDto
from typing import List
class DiseaseService():
    def __init__(self):
        self.Base_Url = "http://127.0.0.1:8000/"
    
    def CreateDisease(self, disease: DiseaseDto):
        try:
            endpoint = self.Base_Url + 'disease/create'
            print(endpoint)
            response = requests.post(endpoint, json=disease.dict())
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Sign data Not created: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def EditDisease(self, disease: DiseaseDto, id: int):
        endpoint = self.Base_Url + f'disease/edit/{id}'
        print(id)
        Disease_dict = {
            "name": disease.name,
            "peligro": disease.peligro
        }
        print(Disease_dict)
        try:
            response = requests.put(endpoint, json=Disease_dict)
            if response.status_code == 500:
                messagebox.showerror("Error", "Error 500: Problema interno del servidor.")
            elif response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Error al editar la enfermedad: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Error desconocido: {e}")


    def SearchById(self, id):
        endpoint = self.Base_Url + f'disease/{id}'
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Sign Not Found: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def Delete(self, id):
        endpoint = self.Base_Url + f'disease/delete/{id}'
        try:
            response = requests.delete(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Sign Not Deleted: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def GetDiseases(self):
        endpoint = self.Base_Url + 'disease'
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Failed to retrieve signs: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def getSymptoms(self,id: int):
        endpoint = self.Base_Url + f'disease/symptoms/{id}'
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Failed to retrieve signs: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")
    
    def getSigns(self,id: int):
        endpoint = self.Base_Url + f'disease/signs/{id}'
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Failed to retrieve signs: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")
    
    def CreateSymptomsList(self,id,data):
        endpoint = self.Base_Url + f'disease/create/symptoms/{id}'
        print(data)
        try:
            response = requests.post(endpoint,json=data)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Failed to retrieve signs: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def CreateSignsList(self,id:int,data:List[int]):
        endpoint = self.Base_Url + f'disease/create/signs/{id}'
        try:
            response = requests.post(endpoint,json=data)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Failed to retrieve signs: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def DeleteSymptoms(self,id:int):
        endpoint = self.Base_Url + f'disease/delete/symptoms/{id}'
        try:
            response = requests.delete(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Failed to retrieve signs: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")
    
    def DeleteSigns(self,id:int):
        endpoint = self.Base_Url + f'disease/delete/signs/{id}'
        try:
            response = requests.delete(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Failed to retrieve signs: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")
