import customtkinter
from dto.User import UserDto,authenticationDto
from controller.AuthController import AuthController
from assets.themes.AdminPalette import AdminTheme

class register(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        self.controller = AuthController()
        self.roles = ['Admin','Doctor','Secretaria']
        self.rolValue = {'Admin':1,'Doctor':2,'Secretaria':3}
        super().__init__(master, **kwargs)
        self.configure(fg_color=AdminTheme['secondary'], corner_radius=15, width=500, height=250)
        self.label = customtkinter.CTkLabel(self, text="crear cuenta", font=("Arial", 18), text_color="white")
        self.label.place(x=20, y=30)
        self.setForm()

    def setForm(self):
        self.name = customtkinter.CTkEntry(self, placeholder_text="Nombre", width=150,text_color='black')
        self.name.configure(fg_color="white", border_color="white")
        self.name.place(x=20,y=80)
        self.firstName = customtkinter.CTkEntry(self, placeholder_text="Apellido paterno", width=150,text_color='black')
        self.firstName.configure(fg_color="white", border_color="white")
        self.firstName.place(x=180,y=80)
        self.SecondName = customtkinter.CTkEntry(self, placeholder_text="Apellido materno", width=150,text_color='black')
        self.SecondName.configure(fg_color="white", border_color="white")
        self.SecondName.place(x=340,y=80)
        self.email = customtkinter.CTkEntry(self, placeholder_text="Correo", width=230,text_color='black')
        self.email.configure(fg_color="white", border_color="white")
        self.email.place(x=20,y=120)
        self.password = customtkinter.CTkEntry(self, placeholder_text="Contraseña", show="*", width=230,text_color='black')
        self.password.configure(fg_color="white", border_color="white")
        self.password.place(x=260,y=120)
        self.phone = customtkinter.CTkEntry(self, placeholder_text="telefono", width=160,text_color='black')
        self.phone.configure(fg_color="white", border_color="white")
        self.phone.place(x=20,y=160)
        self.role = customtkinter.CTkComboBox(self, values=self.roles, command=self.combobox_callback,text_color='black')
        self.role.place(x=190,y=160)
        self.role.configure(fg_color="white", border_color="white")
        self.button = customtkinter.CTkButton(self, text="Crear", width=200, text_color=AdminTheme['primary'], hover_color="#5a5fa9", command=self.createAcount)
        self.button.configure(fg_color=AdminTheme['primary-accent'])
        self.button.place(x=280, y=205)
        
    def combobox_callback(self,choice):
        self.userRole = choice

    def createAcount(self):
        userValue = self.rolValue[self.userRole]
        newAuth = authenticationDto(
            email=self.email.get(),
            password=self.password.get(),
        )
        newUser = UserDto(
            user_name=self.name.get(),
            last_name_f=self.firstName.get(),
            last_name_m=self.SecondName.get(),
            telefono=self.phone.get(),
            user_type=userValue,
        )
        print(self.controller.RegisterUser(newAuth,newUser))

