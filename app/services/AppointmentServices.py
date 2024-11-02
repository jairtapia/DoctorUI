from dto.User import UserDto,authenticationDto
import requests
import json
from tkinter import messagebox

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



