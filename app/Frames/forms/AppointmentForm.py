import customtkinter as ctk
from datetime import datetime,timedelta
from controller.AppointmentController import appointmentController
from assets.themes.AdminPalette import AdminTheme
from dto.Appointments import AppointmentDto
from tkinter import messagebox

class AppointmentForm(ctk.CTkFrame):
    def __init__(self, master,id, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = appointmentController()
        self.DoctorId = id
        self.configure(fg_color=AdminTheme['tertiary'], width=880, height=350)
        if not hasattr(self, '_patients'):
            self._patients = self.controller.getPatients()
            self.patientsList = [{'id': patient['patient_id'], 'name': patient['name']} for patient in self._patients]
        self.patient_names = [patient['name'] for patient in self._patients]
        self.horas_disponibles = [
            "08:00:00", "08:30:00", "09:00:00", "09:30:00", "10:00:00",
            "10:30:00", "11:00:00", "11:30:00", "12:00:00", "12:30:00",
            "13:00:00", "13:30:00", "14:00:00", "14:30:00", "15:00:00",
            "15:30:00", "16:00:00", "16:30:00", "17:00:00"
        ]
        self.fechas_futuras = [(datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(1, 7 + 1)]
        self.create_widgets()

    def create_widgets(self):
        label_title = ctk.CTkLabel(self, text="Formulario de Cita", font=("Arial", 16))
        label_title.pack(pady=10)
        frame_search = ctk.CTkFrame(self, fg_color=AdminTheme['tertiary'])
        frame_search.pack(pady=10)
        self.inputSearch = ctk.CTkEntry(frame_search, placeholder_text="Search", text_color='black', width=500, fg_color='white')
        self.inputSearch.pack(side='left')
        buttonSearch = ctk.CTkButton(frame_search, text="buscar",command=self.setData)
        buttonSearch.pack(side='left', padx=5)
        formFrame = ctk.CTkFrame(self, fg_color=AdminTheme['tertiary'])
        frame_left = ctk.CTkFrame(formFrame, fg_color=AdminTheme['tertiary'])
        frame_left.grid(row=0, column=0, padx=10, pady=5)
        label_paciente = ctk.CTkLabel(frame_left, text="Seleccione el paciente:")
        label_paciente.grid(row=0, column=0, pady=5)
        self.combobox_paciente = ctk.CTkComboBox(frame_left, values=self.patient_names, command=self.combobox_callback)
        self.combobox_paciente.grid(row=1, column=0, pady=5)
        label_fecha = ctk.CTkLabel(frame_left, text="Seleccione la fecha:")
        label_fecha.grid(row=2, column=0, pady=5)
        self.combobox_fecha = ctk.CTkComboBox(frame_left, values=self.fechas_futuras)
        self.combobox_fecha.grid(row=3, column=0, pady=5)
        frame_right = ctk.CTkFrame(formFrame, fg_color=AdminTheme['tertiary'])
        frame_right.grid(row=0, column=1, padx=10, pady=5)
        label_clinica = ctk.CTkLabel(frame_right, text="Seleccione la clínica:")
        label_clinica.grid(row=0, column=0, pady=5)
        self.combobox_clinica = ctk.CTkComboBox(frame_right, values=['1', '2', '3'])
        self.combobox_clinica.grid(row=1, column=0, pady=5)
        label_hora = ctk.CTkLabel(frame_right, text="Seleccione la hora de la cita:")
        label_hora.grid(row=2, column=0, pady=5)
        self.combobox_hora = ctk.CTkComboBox(frame_right, values=self.horas_disponibles)
        self.combobox_hora.grid(row=3, column=0, pady=5)
        formFrame.pack(pady=10)
        OptionFrame = ctk.CTkFrame(self, fg_color=AdminTheme['tertiary'])  
        buttonCreate = ctk.CTkButton(OptionFrame, text="Crear",command=self.enviar_datos)
        buttonCreate.pack(side='left', padx=5)  
        buttonEdit = ctk.CTkButton(OptionFrame, text="Editar",command=self.edit)
        buttonEdit.pack(side='left', padx=5)    
        buttonDelete = ctk.CTkButton(OptionFrame, text="Eliminar",command=self.delete)
        buttonDelete.pack(side='left', padx=5) 
        OptionFrame.pack(pady=10)

    def combobox_callback(self,choice):
        self.patientId = self.get_patient_id_by_name(choice)
        print(self.patientId)

    def get_patient_id_by_name(self,patient_name):
        for patient in self.patientsList:
            if patient['name'] == patient_name:
                return patient['id']
            
    def enviar_datos(self):
        fecha_cita = self.combobox_fecha.get()
        clinica = self.combobox_clinica.get()
        hora_cita = self.combobox_hora.get()
        try:
            cita = AppointmentDto(
                date=fecha_cita,
                time=hora_cita,
                patient_id=self.patientId,
                doctor_id=self.DoctorId,
                clinic_room_id=clinica
            )
            print(cita)
            print(self.controller.create(cita))
        except Exception as e:
                messagebox.showerror("Error", "datos no validos")
    
    def edit(self):
        self.citaId = self.inputSearch.get()
        fecha_cita = self.combobox_fecha.get()
        clinica = self.combobox_clinica.get()
        hora_cita = self.combobox_hora.get()
        try:
            cita = AppointmentDto(
                date=fecha_cita,
                time=hora_cita,
                patient_id=self.patientId,
                doctor_id=self.doctorId,
                clinic_room_id=clinica
            )
            self.appointmentController.edit(cita,self.citaId)
        except Exception as e:
                messagebox.showerror("Error", f"Error al crear la de modal cita: {e}")

    def get_patient_name_by_id(self, patient_id):
        for patient in self.patientsList:
            if patient['id'] == patient_id:
                return patient['name']

    def setData(self):
        try:
            try:
                citaId = self.inputSearch.get()
            except Exception as e:
                messagebox.showerror("Error", f"Error al obtener el ID de la cita: {e}")
            data = self.controller.findById(citaId)
            if data is None:
                messagebox.showerror("Error", "No se encontraron datos para la cita.")
                return
            name_patient = self.get_patient_name_by_id(data['patient_id'])
            self.combobox_paciente.set(name_patient)
            self.combobox_fecha.set(data['date'])
            self.combobox_clinica.set(data['clinic_room_id'])
            self.combobox_hora.set(data['time'])
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener los datos: {e}")

    def delete(self):
        try:
            citaId = self.inputSearch.get()
            self.controller.Delete(citaId)
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener el ID de la cita: {e}")