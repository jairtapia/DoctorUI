import customtkinter
from assets.themes.AdminPalette import AdminTheme
from controller.PatientController import PatientController
class patientsList(customtkinter.CTkScrollableFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master, **kwargs)
        self.MyController = PatientController()
        self.configure(fg_color=AdminTheme['tertiary'], corner_radius=15, width=900, height=300)
        self.grid_rowconfigure(0, weight=1)  # Permitir que la fila 0 se expanda
        self.grid_columnconfigure(0, weight=1)
        self.getAppointments()

    def getAppointments(self):
        content = self.MyController.getPatients() 
        for widget in self.winfo_children():
            widget.destroy()
        if not content:
            customtkinter.CTkLabel(self, text="No se encontraron citas.").pack(pady=10)
            return
        for Patient in content:
            self.create_Patient_card(Patient)

    def create_Patient_card(self, Patient):
        card = customtkinter.CTkFrame(self, corner_radius=10, border_color="gray", border_width=1, fg_color="white")
        card.grid(sticky="ew", padx=10, pady=2)  # Reducir el padding vertical
        customtkinter.CTkLabel(card, text=f"Nombre: {Patient['name']}", text_color="black").grid(row=0, column=1, padx=5, pady=1, sticky="w")  
        customtkinter.CTkLabel(card, text=f"Apellido Paterno: {Patient['last_name_f']}", text_color="black").grid(row=0, column=2, padx=5, pady=1, sticky="w")  
        customtkinter.CTkLabel(card, text=f"Apellido Materno: {Patient['last_name_m']}", text_color="black").grid(row=0, column=3, padx=5, pady=1, sticky="w")  
        customtkinter.CTkLabel(card, text=f"Edad: {Patient['age']}", text_color="black").grid(row=1, column=0, padx=5, pady=1, sticky="w")  
        customtkinter.CTkLabel(card, text=f"Teléfono: {Patient['phone']}", text_color="black").grid(row=1, column=1, padx=5, pady=1, sticky="w")  
        customtkinter.CTkLabel(card, text=f"Dirección: {Patient['address']}", text_color="black").grid(row=1, column=2, padx=5, pady=1, sticky="w")  
        customtkinter.CTkLabel(card, text=f"Estado: {Patient['state']}", text_color="black").grid(row=1, column=3, padx=5, pady=1, sticky="w")  
        customtkinter.CTkButton(card, text="Ver más", command=lambda: self.openPatient(Patient['patient_id'])).grid(row=2, column=0, columnspan=4, pady=1)  

    def openPatient(self,id):
        print(id)
