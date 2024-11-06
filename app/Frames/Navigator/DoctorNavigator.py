import customtkinter as ctk
from tkinter import messagebox
import re
from Frames.DoctorList.Appointments import appointments
from assets.themes.AdminPalette import AdminTheme
from Frames.DoctorList.PatientsList import Patients
from dto.Appointments import AppointmentDto
from controller.AppointmentController import appointmentController
from datetime import datetime,timedelta

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
            self.currentCard = Patients(master=self, id=self.id)
        elif topic == 'Citas':
            self.currentCard = appointments(master=self, id=self.id)
        else:
            if isinstance(self.currentCard, appointments):
                print('creando nueva cita')
                self.create_appointment_window()
            else:
                print('creando paciente')
        self.showCard()

    def create_appointment_window(self):
        # Crear una ventana emergente para agendar una cita
        self.new_window = ctk.CTkToplevel(self)
        self.new_window.title("Nueva Cita")
        self.new_window.geometry("400x500")
        self.patients = self.appointmentController.getPatients()
        self.patientsList = [{'id': patient['patient_id'], 'name': patient['name']} for patient in self.patients]
        patient_names = [patient['name'] for patient in self.patients]
        # ComboBox para seleccionar el nombre del paciente
        label_paciente = ctk.CTkLabel(self.new_window, text="Seleccione el paciente:")
        label_paciente.pack(pady=10)
        combobox_paciente = ctk.CTkComboBox(self.new_window, values=patient_names,command=self.combobox_callback)
        combobox_paciente.pack(pady=10)
        fechas_futuras = [(datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(1, 7 + 1)]
        # Entrada de texto para la fecha de la cita
        label_fecha = ctk.CTkLabel(self.new_window, text="Ingrese la fecha de la cita (YYYY-MM-DD):")
        label_fecha.pack(pady=10)
        entry_fecha = ctk.CTkComboBox(self.new_window, values=fechas_futuras)
        entry_fecha.pack(pady=10)
        # ComboBox para seleccionar la clínica
        label_clinica = ctk.CTkLabel(self.new_window, text="Seleccione la clínica:")
        label_clinica.pack(pady=10)
        combobox_clinica = ctk.CTkComboBox(self.new_window, values=['1','2','3'])
        combobox_clinica.pack(pady=10)
        # Lista de horas disponibles
        horas_disponibles = [
            "08:00:00", "08:30:00", "09:00:00", "09:30:00", "10:00:00",
            "10:30:00", "11:00:00", "11:30:00", "12:00:00", "12:30:00",
            "13:00:00", "13:30:00", "14:00:00", "14:30:00", "15:00:00",
            "15:30:00", "16:00:00", "16:30:00", "17:00:00"
        ]

        # ComboBox para seleccionar la hora de la cita
        label_hora = ctk.CTkLabel(self.new_window, text="Seleccione la hora de la cita:")
        label_hora.pack(pady=10)
        combobox_hora = ctk.CTkComboBox(self.new_window, values=horas_disponibles)
        combobox_hora.pack(pady=10)

        # Función para validar el formato de la fecha
        def validar_fecha(fecha):
            # Expresión regular para el formato YYYY-MM-DD
            patron = r"^\d{4}-\d{2}-\d{2}$"
            if re.match(patron, fecha):
                try:
                    # Verificar si la fecha es válida
                    año, mes, día = map(int, fecha.split('-'))
                    return 1 <= mes <= 12 and 1 <= día <= 31  # Comprobación simple para días y meses
                except ValueError:
                    return False
            return False

        # Función para enviar los datos de la cita
        def enviar_datos():
            fecha_cita = entry_fecha.get()
            clinica = combobox_clinica.get()
            hora_cita = combobox_hora.get()
            if not validar_fecha(fecha_cita):
                messagebox.showerror("Error", "El formato de la fecha es incorrecto. Use YYYY-MM-DD.")
            else:
                try:
                    # Crear el objeto de cita
                    cita = AppointmentDto(
                        date=fecha_cita,
                        time=hora_cita,
                        patient_id=self.patientId,
                        doctor_id=self.id,
                        clinic_room_id=clinica
                    )
                    print(self.appointmentController.create(cita))
                except Exception as e:
                    messagebox.showerror("Error", "datos no validos")
                self.new_window.destroy()

        # Botón para enviar los datos de la cita
        boton_enviar = ctk.CTkButton(self.new_window, text="Agendar Cita", command=enviar_datos)
        boton_enviar.pack(pady=20)

    def combobox_callback(self,choice):
        self.patientId = self.get_patient_id_by_name(choice)
        print(self.patientId)

    def get_patient_id_by_name(self,patient_name):
        for patient in self.patientsList:
            if patient['name'] == patient_name:
                return patient['id']
