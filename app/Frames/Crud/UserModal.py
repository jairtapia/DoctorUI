
import customtkinter

class UserModal(customtkinter.CTkToplevel):
    def __init__(self, master,id=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="#d9d9d9", corner_radius=15, width=400, height=450)
        self.id = id
        self.roles = ['Admin','Doctor','Secretaria']
        self.rolValue = {'Admin':1,'Doctor':2,'Secretaria':3}
        print(self.id)
        if self.id is None:
            self.title = "nuevo usuario"
            self.buttonSend = customtkinter.CTkButton(master=self,text="guardar",command=self.CreateNew)
        self.buttonSend = customtkinter.CTkButton(master=self,text="guardar",command=self.EditUser)
        self.Tittle = "editar Usuario"
        self.label = customtkinter.CTkLabel(master=self, text=self.Tittle, text_color="black", font=("Arial", 20))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.setInputs()

    def setInputs(self):
        self.name = customtkinter.CTkEntry(self, placeholder_text="Nombre", width=150,text_color='black')
        self.name.configure(fg_color="white", border_color="white")
        self.name.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.firstName = customtkinter.CTkEntry(self, placeholder_text="Apellido paterno", width=150,text_color='black')
        self.firstName.configure(fg_color="white", border_color="white")
        self.firstName.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.SecondName = customtkinter.CTkEntry(self, placeholder_text="Apellido materno", width=150,text_color='black')
        self.SecondName.configure(fg_color="white", border_color="white")
        self.SecondName.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.email = customtkinter.CTkEntry(self, placeholder_text="Correo", width=230,text_color='black')
        self.email.configure(fg_color="white", border_color="white")
        self.email.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.password = customtkinter.CTkEntry(self, placeholder_text="Contraseña", show="*", width=230,text_color='black')
        self.password.configure(fg_color="white", border_color="white")
        self.password.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.phone = customtkinter.CTkEntry(self, placeholder_text="telefono", width=160,text_color='black')
        self.phone.configure(fg_color="white", border_color="white")
        self.phone.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.role = customtkinter.CTkComboBox(self, values=self.roles, command=self.combobox_callback,text_color='black')
        self.role.configure(fg_color="white", border_color="white")
        self.role.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.buttonSend.grid(row=8, column=0, padx=10, pady=10, sticky="w")

    def combobox_callback(self,choice):
        self.userRole = choice

    def CreateNew(self):
        print("creando uno nuevo")
        self.master.destroyModal()

    def EditUser(self):
        print(f'editando usuario {self.id}')
        self.master.destroyModal()