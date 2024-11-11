import customtkinter
import pandas as pd
from Frames.Crud.PatientModal import PatientModal
from Frames.Table.DynamicTable import DynamicTable
from Frames.Utils.Utils import Utils
from controller.PatientController import PatientController
from dto.Patient import PatientDto
from tkinter import messagebox

class PatientsCrud(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = PatientController()
        self.table = None
        self.modal = None
        self.configure(fg_color="#d9d9d9", corner_radius=15, width=500, height=550)
        self.label = customtkinter.CTkLabel(master=self, text="Gestor de pacientes", text_color="black", font=("Arial", 20))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.table = None
        self.data = self.controller.getPatients()
        self.updateTable()
        self.Options = Utils(master=self)
        self.Options.grid(row=1, column=0, padx=(10, 2), pady=10, sticky="w")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(2, weight=1)

    def updateTable(self):
        # Crea el DataFrame desde los datos obtenidos
        if isinstance(self.data, dict):
            self.df = pd.DataFrame([self.data])
        elif isinstance(self.data, list) and all(isinstance(i, dict) for i in self.data):
            self.df = pd.DataFrame(self.data)
        elif isinstance(self.data, list) and all(isinstance(i, list) for i in self.data):
            self.df = pd.DataFrame(self.data)
        else:
            self.df = pd.DataFrame()
        if self.table is not None:
            self.table.destroy()
        self.table = DynamicTable(self, dataframe=self.df)
        self.table.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    def search(self):
        # Buscar paciente por ID o nombre
        search_value = self.Options.SearchInput.get()
        if search_value.isdigit():
            search_value = int(search_value)
            valor = self.controller.findById(search_value)
        else:
            valor = self.controller.findByName(search_value)
        self.data = valor
        self.updateTable()

    def updateData(self):
        # Actualizar la tabla después de cualquier cambio
        self.data = self.controller.getPatients()
        self.updateTable()

    def openModal(self, id=None):
        # Abre el modal para editar o crear un nuevo paciente
        if self.modal is None:
            self.modal = PatientModal(master=self, id=id)
            self.modal.protocol("WM_DELETE_WINDOW", self.destroyModal)
            self.modal.grab_set()  # Bloquea interacción con otras ventanas
            self.modal.lift()  # Eleva la ventana modal
            self.modal.focus_set()

    def destroyModal(self):
        self.modal.destroy()
        self.modal = None

    def savePatient(self):
        # Guarda un nuevo paciente con los datos del modal
        patient = PatientDto(
            patient_id=None,  # Para un nuevo paciente, el ID es None
            name=self.modal.name.get(),
            last_name_f=self.modal.firstName.get(),  # Asegúrate de que esta propiedad esté en el formulario
            last_name_m=self.modal.SecondName.get(),  # Asegúrate de que esta propiedad esté en el formulario
            age=int(self.modal.age.get()),  # Asegúrate de que la edad sea un número entero
            phone=self.modal.phone.get(),
            address=self.modal.address.get(),  # Agrega el campo de dirección
            state=self.modal.state.get()  # Agrega el campo de estado
        )
        print(patient)
        result = self.controller.CreatePatient(patient)
        if result:
            messagebox.showinfo("Éxito", "Paciente guardado correctamente.")
        else:
            messagebox.showerror("Error", "No se pudo guardar el paciente.")
        self.destroyModal()
        self.updateData()

    def editPatient(self, id):
        # Editar paciente usando el controlador
        patient = PatientDto(
            patient_id=id,  # Se asigna el ID del paciente que se va a editar
            name=self.modal.name.get(),
            last_name_f=self.modal.firstName.get(),
            last_name_m=self.modal.SecondName.get(),
            age=int(self.modal.age.get()),
            phone=self.modal.phone.get(),
            address=self.modal.address.get(),
            state=self.modal.state.get()
        )
        result = self.controller.EditPatient(patient, id)
        if result:
            messagebox.showinfo("Éxito", "Paciente actualizado correctamente.")
        else:
            messagebox.showerror("Error", "No se pudo actualizar el paciente.")
        self.updateData()

    def delete(self, id):
        # Eliminar paciente usando el controlador
        confirmation = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar este paciente?")
        if confirmation:
            result = self.controller.Delete(id)
            if result:
                messagebox.showinfo("Éxito", "Paciente eliminado correctamente.")
            else:
                messagebox.showerror("Error", "No se pudo eliminar el paciente.")
            self.updateData()
