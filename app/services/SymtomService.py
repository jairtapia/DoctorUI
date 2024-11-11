import requests
import json
from tkinter import messagebox
from dto.Symtom import SymptomDto

class SymptomService():
    def __init__(self):
        self.Base_Url = "http://127.0.0.1:8000/"
    
    def CreateSymptom(self, symptom: SymptomDto):
        try:
            endpoint = self.Base_Url + 'symptoms/create'
            response = requests.post(endpoint, json=symptom.dict())
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Symptom data Not created: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def EditSymptom(self, symptom: SymptomDto, id: int):
        endpoint = self.Base_Url + f'symptoms/edit/{id}'
        try:
            response = requests.put(endpoint, json=symptom.dict())
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Failed to edit symptom: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def SearchById(self, id):
        endpoint = self.Base_Url + f'symptoms/{id}'
        print(endpoint)
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Symptom Not Found: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def Delete(self, id):
        endpoint = self.Base_Url + f'symptoms/delete/{id}'
        try:
            response = requests.delete(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Symptom Not Deleted: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def GetSymptoms(self):
        endpoint = self.Base_Url + 'symptoms'
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Failed to retrieve symptoms: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")