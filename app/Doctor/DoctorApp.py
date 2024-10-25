import customtkinter
from assets.themes.green import ThemeGreen

class DoctorApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x600")  # Tamaño de la ventana principal
        self.title("Doctor inteligente")
        self.configure(fg_color=ThemeGreen['primary'])

