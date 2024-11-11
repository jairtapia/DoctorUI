import customtkinter
import pandas as pd
from Frames.Crud.UserModal import UserModal
from Frames.Utils.Utils import Utils
from controller.UserController import UserController 
from controller.AuthController import AuthController
from Frames.Table.DynamicTable import DynamicTable
from dto.User import UserDto
from dto.User import authenticationDto

class DiseaseCrud(customtkinter.CTkFrame):
    def __init__(self, master,role, **kwargs):
        self.currentRole = role
        super().__init__(master, **kwargs)
        self.controller = UserController()
        self.saveController =AuthController()
        self.table = None
        self.modal = None
        self.configure(fg_color="#d9d9d9", corner_radius=15, width=500, height=550)
        self.label = customtkinter.CTkLabel(master=self, text="Gestor de Enfermedades", text_color="black", font=("Arial", 20))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.data = self.controller.getUsers()
        self.df = pd.DataFrame(self.data)
        self.updateTable()
        self.Options = Utils(master=self)
        self.Options.grid(row=1, column=0, padx=(10, 2), pady=10, sticky="w")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(2, weight=1)
        print(self.currentRole)
        
    def updateTable(self):
        # Asegúrate de que self.data sea una lista de diccionarios o listas
        if isinstance(self.data, dict):
            self.df = pd.DataFrame([self.data])  # Convierte el diccionario en una lista de un solo elemento
        elif isinstance(self.data, list) and all(isinstance(i, dict) for i in self.data):
            self.df = pd.DataFrame(self.data)  # Lista de diccionarios
        elif isinstance(self.data, list) and all(isinstance(i, list) for i in self.data):
            self.df = pd.DataFrame(self.data)  # Lista de listas
        else:
            self.df = pd.DataFrame()  # Crea un DataFrame vacío si no se cumple ninguna condición
        if self.table is not None:
            self.table.destroy()
        self.table = DynamicTable(self,dataframe=self.df)
        self.table.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    def search(self):
        Searchvalue = self.Options.SearchInput.get()
        if Searchvalue.isdigit():
            Searchvalue = int(Searchvalue)
            valor = self.controller.findById(Searchvalue)
        elif isinstance(Searchvalue, str):
            valor = self.controller.findByName(Searchvalue)
        self.data = valor
        self.updateTable()

    def updateData(self):
        self.data = self.controller.getUsers()
        self.updateTable()

    def openModal(self, id=None):
        if self.modal is None:
            self.modal = UserModal(master=self,id = id,role=self.currentRole)
            self.modal.protocol("WM_DELETE_WINDOW", self.destroyModal)
            self.modal.grab_set()  # Para evitar interacción con otras ventanas
            self.modal.lift()  # Elevar la ventana modal
            self.modal.focus_set()

    def destroyModal(self):
        self.modal.destroy()
        self.modal = None

            
    def editUser(self,rol,id):
        usuario = UserDto(
            user_name=self.modal.name.get(),
            last_name_f=self.modal.firstName.get(),
            last_name_m=self.modal.SecondName.get(),
            telefono=self.modal.phone.get(),
            user_type=rol,
        )
        print(id)
        print(self.controller.EditUser(usuario,id))
        if self.currentRole == 1:
            self.editCrd()
        self.destroyModal()
        self.updateData()

    def editCrd(self):
        print(self.modal.email.get())
        print(self.modal.password.get())
    
    def saveUser(self,rol):
        usuario = UserDto(
            user_name=self.modal.name.get(),
            last_name_f=self.modal.firstName.get(),
            last_name_m=self.modal.SecondName.get(),
            telefono=self.modal.phone.get(),
            user_type=rol,
        )
        Credenciales = authenticationDto(
            email =  self.modal.email.get(),
            password = self.modal.password.get()
        )
        self.saveController.RegisterUser(Credenciales,usuario)
        self.destroyModal()
        self.updateData()
        
    
    def delete(self,id):
        self.controller.Delete(id)
        self.updateData()

