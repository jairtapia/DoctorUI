import customtkinter
from assets.themes.AdminPalette import AdminTheme
from Frames.DoctorList.Appointments import appointments
from Frames.Navigator.DoctorNavigator import navigator
from Doctor.DoctorInfo import info

class DoctorApp(customtkinter.CTk):
    def __init__(self,id):
        super().__init__()
        self.id = id
        self.geometry("900x600")  # Tamaño de la ventana principal
        self.title("Doctor inteligente")
        self.configure(fg_color=AdminTheme['primary'])
        self.grid_rowconfigure(0, weight=1)  # Permitir que la fila 0 se expanda
        self.grid_rowconfigure(1, weight=1)  # Permitir que la fila 1 se expanda
        self.grid_columnconfigure(0, weight=1) 
        self.info = info(master=self,id=self.id)
        self.info.grid(row=0, column=0, sticky="nsew", padx=(10,5), pady=10)
        self.navigator = navigator(master=self, id=self.id)
        self.navigator.grid(row=1, column=0, sticky="nsew", padx=(10,5), pady=10)

