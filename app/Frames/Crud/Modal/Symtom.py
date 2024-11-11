import customtkinter as ctk
from tkinter import messagebox
from controller.SymptomController import SymptomController
from assets.themes.AdminPalette import AdminTheme

class SymptomModal(ctk.CTkToplevel):
    def __init__(self, master,id, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.controller = SymptomController()
        self.setInputs()
        self.Symptomid = id
        if self.Symptomid != None:
            self.boton_enviar = ctk.CTkButton(self, text="editar sintoma", command=self.edit)
            self.boton_enviar.grid(row=8, column=0, padx=20, pady=20, sticky="ew")
            self.data = self.controller.search_by_id(self.Symptomid)
            self.setData()
        else:
            self.boton_enviar = ctk.CTkButton(self, text="crear sintoma", command=self.save)
            self.boton_enviar.grid(row=8, column=0, padx=20, pady=20, sticky="ew")
        self.title("Nueva Sintoma")
        self.geometry("200x200")
        self.configure(fg_color=AdminTheme['secondary'],corner_radius=15)

    def setInputs(self):
        # Etiqueta y entrada para el nombre del síntoma
        self.label_titulo = ctk.CTkLabel(self, text="Síntoma", text_color="black", font=("Arial", 16))
        self.label_titulo.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        self.entry_nombre = ctk.CTkEntry(self, placeholder_text="Nombre del síntoma", text_color='black',fg_color='white')
        self.entry_nombre.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.entry_descripcion = ctk.CTkEntry(self, placeholder_text="Descripción del síntoma", text_color='black',fg_color='white')
        self.entry_descripcion.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        # Configurar las columnas para que todos los elementos estén en el centro
        self.grid_columnconfigure(0, weight=1)


    def save(self):
        try:
            self.master.saveSymptom()
        except Exception as e:
            messagebox.showerror("Error", f"Error al crear la cita: {e}")

    def setData(self):
        self.entry_nombre.insert(0,self.data['name'])
        self.entry_descripcion.insert(0,self.data['descripcion'])
        pass


    def edit(self):
        try:
            self.master.editSymptom(self.Symptomid)
        except Exception as e:
            messagebox.showerror("Error", f"Error al crear la de modal cita: {e}")
