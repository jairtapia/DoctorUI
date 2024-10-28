import customtkinter
import pandas as pd
from Frames.Table.DynamicTable import DynamicTable
from Frames.Utils.Utils import Utils

class AppointmentCrud(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="#d9d9d9", corner_radius=15, width=500, height=550)
        self.label = customtkinter.CTkLabel(master=self, text="Gestor de Citas", text_color="black", font=("Arial", 20))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.table = None
        self.data = [
            {'product_id': 1, 'name': 'Laptop', 'category': 'Electronics', 'price': 1000, 'stock_quantity': 50},
            {'product_id': 2, 'name': 'Smartphone', 'category': 'Electronics', 'price': 600, 'stock_quantity': 150},
            {'product_id': 3, 'name': 'Tablet', 'category': 'Electronics', 'price': 300, 'stock_quantity': 200},
            {'product_id': 4, 'name': 'Headphones', 'category': 'Accessories', 'price': 100, 'stock_quantity': 100},
            {'product_id': 5, 'name': 'Smartwatch', 'category': 'Wearables', 'price': 200, 'stock_quantity': 75}
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