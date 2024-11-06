import customtkinter
from controller.PatientController import PatientController
from assets.themes.AdminPalette import AdminTheme
from tkinter import messagebox

class PatientModal(customtkinter.CTkToplevel):
    def __init__(self, master,id, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = PatientController()
        self.geometry("250x370")

        self.title("formulario paciente")  # Establecer el tamaño del modal
        self.configure(fg_color=AdminTheme['secondary'], corner_radius=15)
        self.id = id
        self.roles = ['Admin','Doctor','Secretaria']
        self.rolValue = {'Admin':1,'Doctor':2,'Secretaria':3}
        self.CreateInputs()
        if self.id is None:
            self.Tittle = "nuevo paciente"
            self.buttonSend = customtkinter.CTkButton(master=self,text="guardar",command=self.CreateNew)
        else:
            print(self.id)
            self.buttonSend = customtkinter.CTkButton(master=self,text="guardar",command=self.EditPatient)
            self.Tittle = "editar paciente"
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

    def setInputs(self, patient):
        self.name.insert(0, patient['name'])
        self.firstName.insert(0, patient['last_name_f'])  # Asumiendo que last_name_f es el apellido paterno
        self.SecondName.insert(0, patient['last_name_m'])  # Asumiendo que last_name_m es el apellido materno
        self.age.insert(0, patient['age'])
        self.phone.insert(0, patient['phone'])
        self.address.insert(0, patient['address'])
        self.state.insert(0, patient['state'])

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
        self.age = customtkinter.CTkEntry(self, placeholder_text="Edad", width=150,text_color='black')
        self.age.configure(fg_color="white", border_color="white")
        self.age.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        self.phone = customtkinter.CTkEntry(self, placeholder_text="telefono", width=150,text_color='black')
        self.phone.configure(fg_color="white", border_color="white")
        self.phone.grid(row=6, column=1, padx=10, pady=5, sticky="ew")
        self.address = customtkinter.CTkEntry(self, placeholder_text="Direccion", width=150,text_color='black')
        self.address.configure(fg_color="white", border_color="white")
        self.address.grid(row=7, column=1, padx=10, pady=5, sticky="ew")
        self.state = customtkinter.CTkEntry(self, placeholder_text="Estado", width=150,text_color='black')
        self.state.configure(fg_color="white", border_color="white")
        self.state.grid(row=8, column=1, padx=10, pady=5, sticky="ew")



    def CreateNew(self):
        print("creando uno nuevo")
        self.master.savePatient()

    def EditPatient(self):
        self.master.editPatient(self.id)
