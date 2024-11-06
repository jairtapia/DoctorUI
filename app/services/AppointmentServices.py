import requests
import json
from tkinter import messagebox
from dto.Appointments import AppointmentDto

class appointmentService():
    def __init__(self):
        self.Base_Url = "http://127.0.0.1:8000/"

    def getAppointmentsByDoctor(self,id):
        endpoint = self.Base_Url + f'appointments/{id}'
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"appointments Not Found: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"unknown error: {e}")
    
    def getAppointments(self):
        endpoint = self.Base_Url + f'appointments'
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"appointments Not Found: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"unknown error: {e}")

    def getPatients(self):
        endpoint = self.Base_Url + f'Patients'
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"appointments Not Found: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"unknown error: {e}")
    

    def CreateAppointment(self, cita: AppointmentDto):
        endpoint = self.Base_Url + f'appointments/create'
        cita_dict = cita.dict()
        cita_dict['date'] = cita.date.strftime('%Y-%m-%d')
        cita_dict['time'] = cita.time.strftime('%H:%M:%S') 
        print(cita_dict)  # Aquí puedes ver el formato de los datos antes de enviarlos
        try:
            # Envía el diccionario directamente, sin usar json.dumps
            response = requests.post(endpoint, json=cita_dict)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"appointment Not Created: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"unknown error: {e}")

    def findById(self,id:int):
        endpoint = self.Base_Url + f'appointments/find/{id}'
        try:
            response = requests.get(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"appointments Not Found: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"unknown error: {e}")
    
    def Delete(self, id: int):
        endpoint = self.Base_Url + f'appointments/delete/{id}'
        try:
            response = requests.delete(endpoint)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"appointment Not Found: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"unknown error: {e}")

    def edit(self,cita:AppointmentDto,id:int):
        print(id)
        endpoint = self.Base_Url + f'appointments/update/{id}'
        cita_dict = {
            "date": cita.date.strftime('%Y-%m-%d'),
            "time": cita.time.strftime('%H:%M:%S'),
            "patient_id": cita.patient_id,
            "doctor_id": cita.doctor_id,
            "clinic_room_id": cita.clinic_room_id
        }
        print(cita_dict)  # Aquí puedes ver el formato de los datos antes de enviarlos
        try:
            response = requests.put(endpoint,json=cita_dict)
            if response.status_code == 200:
                return response.json()
            else:
                messagebox.showerror("Error", f"appointment Not Edited: {response.status_code}")
        except Exception as e:
            messagebox.showerror("Error", f"unknown error: {e}")





