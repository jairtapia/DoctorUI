import customtkinter
from assets.themes.AdminPalette import AdminTheme
from Frames.Navigator.navigator import navigator
from Frames.Crud.Users import UsersCrud
from Frames.Crud.Appointment import AppointmentCrud
from Frames.Crud.Patients import PatientsCrud
from Frames.Crud.Disease import DiseaseCrud
from Frames.Crud.Signs import SignsCrud
from Frames.Crud.Symptoms import SymptomsCrud


class AdminApp(customtkinter.CTk):
    def __init__(self,rol, **kwargs):
        super().__init__()
        self.CurrentRole = rol
        self.geometry("900x600")  # Tamaño de la ventana principal
        self.title("gestor de Administrador")
        self.configure(fg_color=AdminTheme['background'])
        self.navigator = navigator(master=self)
        self.navigator.grid(row=0, column=0, sticky="nsew", padx=(10,5), pady=10)
        self.grid_columnconfigure(0, weight=0)  # Evitar que crezca demasiado
        self.navigator.configure(width=200)  # Ancho máximo deseado del menú

        # Frame de contenido (CRUD)
        self.currentCrud = UsersCrud(master=self,role=self.CurrentRole)
        self.ShowCurrentCrud()

        # Configuración dinámica del CRUD (expandible)
        self.grid_columnconfigure(1, weight=1)  # Permitir expansión del CRUD
        self.grid_rowconfigure(0, weight=1) 

    def ShowCurrentCrud(self):
        self.currentCrud.grid(row=0, column=1, sticky="nsew",pady = 10,padx=(5,10))

    def updateCrud(self, message):
        self.currentCrud.destroy()
        match message:
            case "Usuarios":
                self.currentCrud = UsersCrud(master=self, role=self.CurrentRole)
            case "Pacientes":
                self.currentCrud = PatientsCrud(master=self)
            case "Citas":
                self.currentCrud = AppointmentCrud(master=self)
            case "Enfermedades":
                self.currentCrud = DiseaseCrud(master=self, role=self.CurrentRole)
            case "Signos":
                self.currentCrud = SignsCrud(master=self, role=self.CurrentRole)
            case "Sintomas":
                self.currentCrud = SymptomsCrud(master=self, role=self.CurrentRole)
            case "Exit":
                self.destroy()
        self.ShowCurrentCrud()