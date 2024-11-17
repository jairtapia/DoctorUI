import requests
import json
from tkinter import messagebox
from dto.Diagnostic import DiagnosticDto
from typing import List

class DiagnosticService():
    def __init__(self):
        self.Base_Url = "http://127.0.0.1:8000/"
    
    def Creatediagnostic(self, diagnostic: DiagnosticDto):
        try:
            endpoint = self.Base_Url + 'diagnostico/create'
            diagnostic_dict = {
                "paciente": diagnostic.paciente,
                "medico": diagnostic.medico,
                "fecha": diagnostic.fecha.strftime('%Y-%m-%d'),
                "descripcion": diagnostic.descripcion,
                "receta": diagnostic.receta,
                "enfermedad": diagnostic.enfermedad,
                "estado": diagnostic.estado
            }
            diagnostic_json = json.dumps(diagnostic_dict)
            print(diagnostic_json) 
            # Envía el diccionario directamente
            response = requests.post(endpoint, data=diagnostic_json)
            # Verifica la respuesta
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                messagebox.showerror("Error", f"no se creo {response.status_code}, {response.text}")
            else:
                messagebox.showerror("Error", f"Sign data not created: {response.status_code}, {response.text}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def Editdiagnostic(self, diagnostic: DiagnosticDto, id: int):
        endpoint = self.Base_Url + f'diagnostic/edit/{id}'
        print(id)
        print(diagnostic)
        try:
            response = requests.put(endpoint, json=diagnostic)
            if response.status_code == 500:
                messagebox.showerror("Error", "Error 500: Problema interno del servidor.")
            elif response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Error al editar la enfermedad: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Error desconocido: {e}")


    def SearchById(self, id):
        endpoint = self.Base_Url + f'diagnostic/{id}'
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Sign Not Found: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def Delete(self, id):
        endpoint = self.Base_Url + f'diagnostic/delete/{id}'
        try:
            response = requests.delete(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Sign Not Deleted: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def Getdiagnostics(self):
        endpoint = self.Base_Url + 'diagnostic'
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Failed to retrieve signs: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")
    
    def updateHitoric(self,diagnostico:int,paciente:int):
        endpoint = self.Base_Url + f'diagnostic/patient'
        try:
            dato_dict = {
                "patient_id": paciente,
                "diagnostic_id": diagnostico
            }
            response = requests.post(endpoint,json=dato_dict)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Failed to retrieve signs: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def getHistoric(self,id:int):
        endpoint = self.Base_Url + f'diagnostic/patient/{id}'
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Failed to retrieve signs: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

