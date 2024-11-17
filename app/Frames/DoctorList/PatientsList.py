import customtkinter
from assets.themes.AdminPalette import AdminTheme
from controller.PatientController import PatientController
class Patients(customtkinter.CTkScrollableFrame):
    def __init__(self, master, id,**kwargs):
        super().__init__(master, **kwargs)
        self.MyController = PatientController()
        self.id = id
        self.configure(fg_color=AdminTheme['tertiary'], corner_radius=15, width=900, height=300)
        self.grid_rowconfigure(0, weight=1)  # Permitir que la fila 0 se expanda
        self.grid_columnconfigure(0, weight=1)
        self.getPatients()

    def getPatients(self):
        content = self.MyController.getPatients() 
        for widget in self.winfo_children():
            widget.destroy()
        if not content:
            customtkinter.CTkLabel(self, text="No se encontraron citas.").pack(pady=10)
            return
        for appointment in content:
            self.create_appointment_card(appointment)

    def create_appointment_card(self, appointment):
        card = customtkinter.CTkFrame(self, corner_radius=10, border_color="gray", border_width=1, fg_color="white")
        card.grid(sticky="ew", padx=10, pady=2)  # Reducir el padding vertical
        customtkinter.CTkLabel(card, text=f"Fecha: {appointment['date']}", text_color="black").grid(row=0, column=0, padx=5, pady=1, sticky="w")  
        customtkinter.CTkLabel(card, text=f"Hora: {appointment['time']}", text_color="black").grid(row=0, column=1, padx=5, pady=1, sticky="w")  
        customtkinter.CTkLabel(card, text=f"Paciente: {appointment['patient']['name']} {appointment['patient']['lastname']}", text_color="black").grid(row=0, column=2, padx=5, pady=1, sticky="w")  
        customtkinter.CTkLabel(card, text=f"Sala: {appointment['clinic_room']['numero']}", text_color="black").grid(row=0, column=3, padx=5, pady=1, sticky="w")  
        customtkinter.CTkButton(card, text="Ver historial", command=lambda: self.openAppointment(appointment['id'])).grid(row=1, column=0, columnspan=4, pady=1)  

    def openAppointment(self,id):
        print(id)
