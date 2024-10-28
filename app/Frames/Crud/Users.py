import customtkinter
import pandas as pd
from Frames.Crud.UserModal import UserModal,Utils
from controller.UserController import UserController
class UsersCrud(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = UserController()
        self.modal = None
        self.configure(fg_color="#d9d9d9", corner_radius=15, width=500, height=550)
        self.label = customtkinter.CTkLabel(master=self, text="Users Crud", text_color="black", font=("Arial", 20))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.data = self.controller.getUsers()
        self.df = pd.DataFrame(self.data)
        self.Options = Utils(master=self)
        self.Options.grid(row=1, column=0, padx=(10, 2), pady=10, sticky="w")
        self.table = DynamicTable(self, dataframe=self.df)
        self.table.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(2, weight=1)
        
    def search(self):
        Searchvalue = self.Options.SearchInput.get()
        if Searchvalue.isdigit():
            print(f"es un numero entero: {Searchvalue}")
            Searchvalue = int(Searchvalue)  # Convertir la cadena a un número entero si es necesario
        elif isinstance(Searchvalue, str):
            print(f"es una cadena: {Searchvalue}")
        self.openModal(Searchvalue)

    def openModal(self, id=None):
        if self.modal is None:
            self.modal = UserModal(master=self)
    
    def delete(self,id):
        self.controller.Delete(id)

class DynamicTable(customtkinter.CTkFrame):
    def __init__(self, master, dataframe, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(fg_color="#d9d9d9", corner_radius=15, width=450, height=500)
            # Crear un frame contenedor con scrollbar
        container = customtkinter.CTkScrollableFrame(self)
        container.pack(expand=True, fill="both", padx=10, pady=10)
            # Obtener los nombres de las columnas y las filas del DataFrame
        headers = dataframe.columns.tolist()
        data = dataframe.values.tolist()
        headers.append("editar")
        headers.append("eliminar")
        for col_index, header in enumerate(headers):
            header_label = customtkinter.CTkLabel(container, text=header, fg_color="#2A4B7C", 
                                        text_color="white", padx=5, pady=5, corner_radius=5)
            header_label.grid(row=0, column=col_index, sticky="nsew", padx=2, pady=2)
        for row_index, row in enumerate(data):
            for col_index, cell in enumerate(row):
                cell_label = customtkinter.CTkLabel(container, text=str(cell), padx=5, pady=5)
                cell_label.grid(row=row_index + 1, column=col_index, sticky="nsew", padx=2, pady=2)
            edit_button = customtkinter.CTkButton(container, text="Editar", 
                                                  command=lambda r=row: self.edit_row(r), width=50)
            edit_button.grid(row=row_index + 1, column=len(headers) - 2, sticky="nsew", padx=2, pady=2)
            delete_button = customtkinter.CTkButton(container, text="Eliminar", 
                                                    command=lambda r=row: self.delete_row(r), width=50)
            delete_button.grid(row=row_index + 1, column=len(headers) - 1, sticky="nsew", padx=2, pady=2)

    def edit_row(self, row):
        id = row[0]
        self.master.openModal(id)

    def delete_row(self, row):
        id = row[0]
        self.master.delete(id)
