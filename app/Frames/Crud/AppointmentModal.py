import customtkinter as ctk
from datetime import datetime, timedelta
import re
from tkinter import messagebox
from controller.AppointmentController import appointmentController
from dto.Appointments import AppointmentDto
from assets.themes.AdminPalette import AdminTheme


class AppointmentScheduler(ctk.CTkToplevel):
    def __init__(self, master, citaId, doctorId, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.citaId = citaId
        self.doctorId = doctorId
        self.horas_disponibles = [
            "08:00:00", "08:30:00", "09:00:00", "09:30:00", "10:00:00",
            "10:30:00", "11:00:00", "11:30:00", "12:00:00", "12:30:00",
            "13:00:00", "13:30:00", "14:00:00", "14:30:00", "15:00:00",
            "15:30:00", "16:00:00", "16:30:00", "17:00:00"
        ]
        self.appointmentController = appointmentController()
        self.patients = self.appointmentController.getPatients()
        self.patientsList = [{'id': patient['patient_id'], 'name': patient['name']} for patient in self.patients]
        self.setInputs()
        if self.citaId != None:
            self.boton_enviar = ctk.CTkButton(self, text="editar Cita", command=self.edit)
            self.boton_enviar.grid(row=8, column=0, padx=20, pady=20, sticky="ew")
            self.data = self.appointmentController.findById(self.citaId)
            self.setData()
        else:
            self.boton_enviar = ctk.CTkButton(self, text="Agendar Cita", command=self.save)
            self.boton_enviar.grid(row=8, column=0, padx=20, pady=20, sticky="ew")
        
        self.title("Nueva Cita")
        self.geometry("400x500")
        self.configure(fg_color=AdminTheme['secondary'],corner_radius=15)

    def setInputs(self):
        # Etiqueta y ComboBox para seleccionar el paciente
        self.label_paciente = ctk.CTkLabel(self, text="Seleccione el paciente:", text_color="black", font=("Arial", 14))
        self.label_paciente.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        self.patient_names = [patient['name'] for patient in self.patientsList]
        self.combobox_paciente = ctk.CTkComboBox(self, values=self.patient_names, command=self.combobox_callback, text_color='black')
        self.combobox_paciente.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        # Etiqueta y ComboBox para seleccionar la fecha
        self.label_fecha = ctk.CTkLabel(self, text="Seleccione la fecha:", text_color="black", font=("Arial", 14))
        self.label_fecha.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.fechas_futuras = [(datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(1, 8)]
        self.combobox_fecha = ctk.CTkComboBox(self, values=self.fechas_futuras, text_color='black')
        self.combobox_fecha.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        # Etiqueta y ComboBox para seleccionar la clínica
        self.label_clinica = ctk.CTkLabel(self, text="Seleccione la clínica:", text_color="black", font=("Arial", 14))
        self.label_clinica.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
        self.combobox_clinica = ctk.CTkComboBox(self, values=['1', '2', '3'], text_color='black')
        self.combobox_clinica.grid(row=5, column=0, padx=20, pady=10, sticky="ew")

        # Etiqueta y ComboBox para seleccionar la hora
        self.label_hora = ctk.CTkLabel(self, text="Seleccione la hora:", text_color="black", font=("Arial", 14))
        self.label_hora.grid(row=6, column=0, padx=20, pady=10, sticky="ew")
        self.combobox_hora = ctk.CTkComboBox(self, values=self.horas_disponibles, text_color='black')
        self.combobox_hora.grid(row=7, column=0, padx=20, pady=10, sticky="ew")
        # Configurar las columnas para que todos los elementos estén en el centro
        self.grid_columnconfigure(0, weight=1)

    def combobox_callback(self, choice):
        self.patientId = self.get_patient_id_by_name(choice)
        print(self.patientId)

    def get_patient_id_by_name(self, patient_name):
        for patient in self.patientsList:
            if patient['name'] == patient_name:
                return patient['id']
            
    def get_patient_name_by_id(self, patient_id):
        for patient in self.patientsList:
            if patient['id'] == patient_id:
                return patient['name']


    def validar_fecha(self, fecha):
        patron = r"^\d{4}-\d{2}-\d{2}$"
        if re.match(patron, fecha):
            try:
                año, mes, día = map(int, fecha.split('-'))
                return 1 <= mes <= 12 and 1 <= día <= 31
            except ValueError:
                return False
        return False

    def save(self):
        fecha_cita = self.combobox_fecha.get()
        clinica = self.combobox_clinica.get()
        hora_cita = self.combobox_hora.get()
        if not self.validar_fecha(fecha_cita):
            messagebox.showerror("Error", "El formato de la fecha es incorrecto. Use YYYY-MM-DD.")
        else:
            try:
                # Crear el objeto de cita
                cita = AppointmentDto(
                    date=fecha_cita,
                    time=hora_cita,
                    patient_id=self.patientId,
                    doctor_id=self.doctorId,
                    clinic_room_id=clinica
                )
                # Llamar al método de creación de cita
                self.appointmentController.create(cita)
                messagebox.showinfo("Éxito", "Cita agendada correctamente.")
                self.master.updateData()
                self.master.destroyModal()
            except Exception as e:
                messagebox.showerror("Error", f"Error al crear la cita: {e}")

    def setData(self):
        name_patient = self.get_patient_name_by_id(self.data['patient_id'])
        print(name_patient)
        self.combobox_paciente.set(name_patient)
        self.combobox_fecha.set(self.data['date'])
        self.combobox_clinica.set(self.data['clinic_room_id'])
        self.combobox_hora.set(self.data['time'])


    def edit(self):
        fecha_cita = self.combobox_fecha.get()
        clinica = self.combobox_clinica.get()
        hora_cita = self.combobox_hora.get()
        if not self.validar_fecha(fecha_cita):
            messagebox.showerror("Error", "El formato de la fecha es incorrecto. Use YYYY-MM-DD.")
        else:
            try:
                # Crear el objeto de cita
                cita = AppointmentDto(
                    date=fecha_cita,
                    time=hora_cita,
                    patient_id=self.patientId,
                    doctor_id=self.doctorId,
                    clinic_room_id=clinica
                )
                print(cita)
                # Llamar al método de creación de cita
                self.appointmentController.edit(cita,self.citaId)
                self.master.updateData()
                self.master.destroyModal()
            except Exception as e:
                messagebox.showerror("Error", f"Error al crear la de modal cita: {e}")
