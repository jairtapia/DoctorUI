import customtkinter as ctk
from tkinter import messagebox
from controller.DiseaseController import DiseaseController
from controller.SymptomController import SymptomController
from controller.SignController import SignController
from dto.Disease import DiseaseDto
from assets.themes.AdminPalette import AdminTheme
from Frames.Box.DynamicBox import Box

class DiseaseModal(ctk.CTkToplevel):
    def __init__(self, master,id, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.controller = DiseaseController()
        self.controllerSymptoms = SymptomController()
        self.controllerSigns = SignController()
        self.DiseaseId = id
        self.setInputs()
        if self.DiseaseId != None:
            self.boton_enviar = ctk.CTkButton(self, text="editar enfermedad", command=self.edit)
            self.boton_enviar.grid(row=8, column=1, padx=20, pady=20, sticky="ew")
            self.data = self.controller.findById(self.DiseaseId)
            self.setData()
        else:
            self.boton_enviar = ctk.CTkButton(self, text="crear enfermedad", command=self.save)
            self.boton_enviar.grid(row=8, column=1, padx=20, pady=20, sticky="ew")
        self.title("Nueva enfermedad")
        self.geometry("730x450")
        self.configure(fg_color=AdminTheme['secondary'],corner_radius=15)

    def setInputs(self):
        # Etiqueta y entrada para el nombre del síntoma
        self.label_titulo = ctk.CTkLabel(self, text="Enfermedad", text_color="black", font=("Arial", 16))
        self.label_titulo.grid(row=0, column=1, padx=20, pady=10, sticky="ew")
        self.entry_nombre = ctk.CTkEntry(self, placeholder_text="Nombre enfermedad", text_color='black',fg_color='white')
        self.entry_nombre.grid(row=1, column=1, padx=20, pady=10, sticky="ew")
        self.entry_peligro = ctk.CTkEntry(self, placeholder_text="valor de peligro", text_color='black',fg_color='white')
        self.entry_peligro.grid(row=2, column=1, padx=20, pady=10, sticky="ew")
        self.SymptomsBox = Box(master=self,text='sintomas',selected=self.controller.getDiseaseSymptoms(self.DiseaseId),data=self.controllerSymptoms.get_symptoms())
        self.SymptomsBox.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        self.SingsBox = Box(master=self,text='signos',selected=self.controller.getDiseaseSigns(self.DiseaseId),data=self.controllerSigns.GetSigns())
        self.SingsBox.grid(row=3, column=2, padx=20, pady=10, sticky="ew")
        self.grid_columnconfigure(0, weight=1)
    
    def getListSympons(self):
        return self.SymptomsBox.getValuesIDs()
    
    def getListSigns(self):
        return self.SingsBox.getValuesIDs()

    def save(self):
        try:
            enfermedad = DiseaseDto(
                name=self.entry_nombre.get(),
                peligro=self.entry_peligro.get()
            )
            print(enfermedad)
            self.master.saveData(enfermedad,self.getListSympons(),self.getListSigns())

        except Exception as e:
            messagebox.showerror("Error", f"Error al crear la cita: {e}")

    def setData(self):
        self.entry_nombre.insert(0, self.data['name'])
        self.entry_peligro.insert(0, self.data['peligro'])

    def edit(self):
        try:
            enfermedad = DiseaseDto(
                name=self.entry_nombre.get(),
                peligro=self.entry_peligro.get()
            )
            self.master.EditData(enfermedad,self.DiseaseId,self.getListSympons(),self.getListSigns())
        except Exception as e:
            messagebox.showerror("Error", f"Error al crear la de modal cita: {e}")
