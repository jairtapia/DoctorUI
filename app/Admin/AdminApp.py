import customtkinter
from assets.themes.green import ThemeGreen
from Frames.Navigator.navigator import navigator
from Frames.Crud.Users import UsersCrud

class AdminApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x600")  # Tamaño de la ventana principal
        self.title("gestor de Administrador")
        self.configure(fg_color=ThemeGreen['primary'])
        self.navigator = navigator(master=self)
        self.navigator.grid(row=0, column=0, sticky="ns",pady = 10,padx=5)
        self.currentCrud = UsersCrud(master=self)
        self.currentCrud.grid(row=0, column=1, sticky="nsew",pady = 10,padx=5)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)
        self.grid_rowconfigure(0,weight=1)

