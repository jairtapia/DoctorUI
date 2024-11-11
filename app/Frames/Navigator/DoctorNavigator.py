import customtkinter as ctk
from tkinter import messagebox
import re
from Frames.DoctorList.Appointments import appointments
from assets.themes.AdminPalette import AdminTheme
from Frames.DoctorList.Patients import patientsList
from controller.AppointmentController import appointmentController
from datetime import datetime,timedelta
from Frames.forms.PatientForm import PatientForm
from Frames.forms.AppointmentForm import AppointmentForm


class navigator(ctk.CTkFrame):
    def __init__(self, master, id, **kwargs):
        super().__init__(master, **kwargs)
        self.appointmentController = appointmentController()
        self.id = id
        print(id)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.configure(fg_color="#d9d9d9", corner_radius=15, width=880, height=350)
        self.buttonContainer = ctk.CTkFrame(master=self)
        self.setButtons()
        self.buttonContainer.grid(row=0, column=0, padx=10, pady=5)
        self.currentCard = appointments(master=self, id=self.id)
        self.showCard()

    def showCard(self):
        self.currentCard.grid(row=1, column=0, padx=10, pady=5)

    def setButtons(self):
        self.buttonContainer.configure(fg_color=AdminTheme['primary'], corner_radius=15, width=700, height=50)
        self.buttonappointments = ctk.CTkButton(master=self.buttonContainer, text='Citas', command=lambda: self.SwitchCard('Citas'))
        self.buttonPatients = ctk.CTkButton(master=self.buttonContainer, text='Pacientes', command=lambda: self.SwitchCard('Pacientes'))
        self.buttonNew = ctk.CTkButton(master=self.buttonContainer, text='Nuevo', command=lambda: self.SwitchCard('Nuevo'))
        self.buttonappointments.grid(row=0, column=0, padx=10, pady=5)
        self.buttonPatients.grid(row=0, column=1, padx=10, pady=5)
        self.buttonNew.grid(row=0, column=2, padx=10, pady=5)

    def SwitchCard(self, topic):
        self.currentCard.destroy()
        if topic == 'Pacientes':
            self.currentCard = patientsList(master=self)
        elif topic == 'Citas':
            self.currentCard = appointments(master=self, id=self.id)
        else:
            if isinstance(self.currentCard, appointments):
                self.currentCard = AppointmentForm(master = self,id=self.id)
            else:
                self.currentCard = PatientForm(master = self)
        self.showCard()

