from dto.Patient import PatientDto
import requests
import json
from tkinter import messagebox

class PatientsService():
    def __init__(self):
        self.Base_Url = "http://127.0.0.1:8000/"

    def CreatePatient(self, patient: PatientDto):
        try:
            endpoint = self.Base_Url + 'Patient/create'
            response = requests.post(endpoint, json=patient.dict())
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Patient data Not created: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def EditPatient(self, patient: PatientDto, id: int):
        endpoint = self.Base_Url + f'Patient/edit/patient_id?id={id}'
        try:
            response = requests.put(endpoint, json=patient.dict())
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Failed to edit patient: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def SearchByName(self, name):
        endpoint = self.Base_Url + f'Patient/find/name/fname?name={name}'
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Patient Not Found: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def SearchById(self, id):
        endpoint = self.Base_Url + f'Patient/find/patient_id?id={id}'
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Patient Not Found: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def Delete(self, id):
        endpoint = self.Base_Url + f'Patient/delete/patient_id?id={id}'
        try:
            response = requests.delete(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Patient Not Deleted: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def GetPatients(self):
        endpoint = self.Base_Url + 'Patients'
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"Bad Request: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")
