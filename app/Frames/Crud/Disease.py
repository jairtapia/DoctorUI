import customtkinter
import pandas as pd
from Frames.Crud.Modal.Disease import DiseaseModal
from Frames.Utils.Utils import Utils
from controller.DiseaseController import DiseaseController
from Frames.Table.DynamicTable import DynamicTable
from dto.Disease import DiseaseDto

class DiseaseCrud(customtkinter.CTkFrame):
    def __init__(self, master,role, **kwargs):
        self.currentRole = role
        super().__init__(master, **kwargs)
        self.controller = DiseaseController()
        self.table = None
        self.modal = None
        self.configure(fg_color="#d9d9d9", corner_radius=15, width=500, height=550)
        self.label = customtkinter.CTkLabel(master=self, text="Gestor de Enfermedades", text_color="black", font=("Arial", 20))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.data = self.controller.GetDiseases()
        self.df = pd.DataFrame(self.data)
        self.updateTable()
        self.Options = Utils(master=self)
        self.Options.grid(row=1, column=0, padx=(10, 2), pady=10, sticky="w")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
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
        self.data = self.controller.GetDiseases()
        self.updateTable()

    def openModal(self, id=None):
        if self.modal is None:
            self.modal = DiseaseModal(master=self,id = id)
            self.modal.protocol("WM_DELETE_WINDOW", self.destroyModal)
            self.modal.grab_set()  # Para evitar interacción con otras ventanas
            self.modal.lift()  # Elevar la ventana modal
            self.modal.focus_set()

    def destroyModal(self):
        self.modal.destroy()
        self.modal = None

    def EditData(self,Disease:DiseaseDto,id,ListSymptoms,ListSigns):
        if self.controller.EditDiesase(Disease,id):
            if self.controller.DeleteDiseaseSigns(id):
                self.controller.createDiseaseSigns(id,ListSigns)
            if self.controller.DeleteDiseaseSymptoms(id):
                self.controller.createDiseaseSymptoms(id,ListSymptoms)
        self.destroyModal()
        self.updateData()

    def saveData(self, Disease, ListSymptoms, ListSigns):
        idData = self.controller.CreateDisease(Disease)['id']
        if idData:
            self.controller.createDiseaseSymptoms(idData, ListSymptoms)
            self.controller.createDiseaseSigns(idData, ListSigns)
        self.destroyModal()
        self.updateData()

    def delete(self,id):
        if self.controller.DeleteDiseaseSymptoms(id) and self.controller.DeleteDiseaseSigns(id):
            self.controller.Delete(id)
        self.updateData()

