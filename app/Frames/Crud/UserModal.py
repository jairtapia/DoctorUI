import customtkinter
from controller.UserController import UserController
from assets.themes.AdminPalette import AdminTheme

class UserModal(customtkinter.CTkToplevel):
    def __init__(self, master,id, **kwargs):
        self.controller = UserController()
        super().__init__(master, **kwargs)
        self.geometry("250x370")
        self.title("formulario usuario")  # Establecer el tamaño del modal
        self.configure(fg_color=AdminTheme['secondary'], corner_radius=15)
        self.id = id
        self.roles = ['Admin','Doctor','Secretaria']
        self.rolValue = {'Admin':1,'Doctor':2,'Secretaria':3}
        self.CreateInputs()
        if self.id is None:
            self.Tittle = "nuevo usuario"
            self.buttonSend = customtkinter.CTkButton(master=self,text="guardar",command=self.CreateNew)
        else:
            print(self.id)
            self.buttonSend = customtkinter.CTkButton(master=self,text="guardar",command=self.EditUser)
            self.Tittle = "editar Usuario"
            user = self.controller.findById(self.id)
            print(user)
            self.setInputs(user)
        self.label = customtkinter.CTkLabel(master=self, text=self.Tittle, text_color="black", font=("Arial", 20))
        self.label.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
        self.buttonSend.grid(row=8, column=1, padx=10, pady=10, sticky="ew")
        
        # Configurar las columnas para que todos los elementos estén en el centro
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def setInputs(self,user):
        self.name.insert(0, user['user_name'])
        self.firstName.insert(0, user['last_name_f'])
        self.SecondName.insert(0, user['last_name_m'])
        self.phone.insert(0, user['telefono'])

    def CreateInputs(self):
        self.name = customtkinter.CTkEntry(self, placeholder_text="Nombre", width=150,text_color='black')
        self.name.configure(fg_color="white", border_color="white")
        self.name.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        self.firstName = customtkinter.CTkEntry(self, placeholder_text="Apellido paterno", width=150,text_color='black')
        self.firstName.configure(fg_color="white", border_color="white")
        self.firstName.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        self.SecondName = customtkinter.CTkEntry(self, placeholder_text="Apellido materno", width=150,text_color='black')
        self.SecondName.configure(fg_color="white", border_color="white")
        self.SecondName.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        self.email = customtkinter.CTkEntry(self, placeholder_text="Correo", width=150,text_color='black')
        self.email.configure(fg_color="white", border_color="white")
        self.email.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        self.password = customtkinter.CTkEntry(self, placeholder_text="Contraseña", show="*", width=150,text_color='black')
        self.password.configure(fg_color="white", border_color="white")
        self.password.grid(row=5, column=1, padx=10, pady=5, sticky="ew")
        self.phone = customtkinter.CTkEntry(self, placeholder_text="telefono", width=150,text_color='black')
        self.phone.configure(fg_color="white", border_color="white")
        self.phone.grid(row=6, column=1, padx=10, pady=5, sticky="ew")
        self.role = customtkinter.CTkComboBox(self, values=self.roles, command=self.combobox_callback,text_color='black')
        self.role.configure(fg_color="white", border_color="white")
        self.role.grid(row=7, column=1, padx=10, pady=5, sticky="ew")
        

    def combobox_callback(self,choice):
        self.userRole = choice

    def CreateNew(self):
        print("creando uno nuevo")
        self.master.saveUser(self.rolValue[self.userRole])

    def EditUser(self):
        print(f'editando usuario {self.id}')
        self.master.editUser(self.rolValue[self.userRole],self.id)