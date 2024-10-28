import customtkinter
import pandas as pd
from Frames.Table.DynamicTable import DynamicTable
from Frames.Utils.Utils import Utils

class PatientsCrud(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="#d9d9d9", corner_radius=15, width=500, height=550)
        self.label = customtkinter.CTkLabel(master=self, text="Gestor de pacientes", text_color="black", font=("Arial", 20))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.table = None
        self.data = [
            {'employee_id': 101, 'name': 'John Doe', 'department': 'Sales', 'salary': 50000, 'employment_status': 'Active'},
            {'employee_id': 102, 'name': 'Jane Smith', 'department': 'HR', 'salary': 60000, 'employment_status': 'Active'},
            {'employee_id': 103, 'name': 'Alice Johnson', 'department': 'IT', 'salary': 70000, 'employment_status': 'Inactive'},
            {'employee_id': 104, 'name': 'Robert Brown', 'department': 'Finance', 'salary': 80000, 'employment_status': 'Active'},
            {'employee_id': 105, 'name': 'Linda White', 'department': 'Marketing', 'salary': 55000, 'employment_status': 'Inactive'}
        ]
        self.updateTable()
        self.Options = Utils(master=self)
        self.Options.grid(row=1, column=0, padx=(10, 2), pady=10, sticky="w")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(2, weight=1)

    def setInputs(self):
        pass

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

