import customtkinter
from assets.themes.AdminPalette import AdminTheme
from Admin.AdminApp import AdminApp
from Doctor.DoctorApp import DoctorApp
from controller.AuthController import AuthController
from dto.User import authenticationDto,UserDto
from tkinter import messagebox

class login(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = AuthController()
        self.configure(fg_color=AdminTheme['secondary'], corner_radius=15, width=500, height=250)
        self.label = customtkinter.CTkLabel(self, text="Iniciar Sesión", font=("Arial", 18), text_color="white")
        self.label.place(x=20, y=30)
        self.generate_input()

    def generate_input(self):
        """Genera entradas de email y contraseña."""
        self.email = customtkinter.CTkEntry(self, placeholder_text="Email", width=400,text_color=AdminTheme['secondary'])
        self.email.configure(fg_color="white", border_color="white")
        self.email.place(x=20, y=80)
        self.password = customtkinter.CTkEntry(self, placeholder_text="Contraseña", show="*", width=400,text_color=AdminTheme['secondary'])
        self.password.configure(fg_color="white", border_color="white")
        self.password.place(x=20, y=130)
        # Botón para iniciar sesión
        self.button = customtkinter.CTkButton(self, text="Entrar", width=200, text_color=AdminTheme['primary'], hover_color="#5a5fa9", command=self.getin)
        self.button.configure(fg_color=AdminTheme['primary-accent'])
        self.button.place(x=280, y=205)
    
    def getin(self):
        Myloggin = authenticationDto(
            email=self.email.get(),
            password=self.password.get()
        )
        login = self.controller.login(Myloggin)
        if login is not None:
            self.master.destroy()
            if login['user_type'] == 1:
                newWindow = AdminApp(rol=1)
            elif login['user_type'] == 3:
                newWindow = AdminApp(rol=3)
            elif login['user_type'] == 2:
                newWindow = DoctorApp(id=login['user_id'])
            newWindow.mainloop()
            

