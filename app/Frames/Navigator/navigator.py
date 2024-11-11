import customtkinter

class navigator(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="#d9d9d9", corner_radius=15, width=300, height=550)
        self.SetButtons()

    def SetCurrentButton(self):
        pass
    
    def SetButtons(self):
        self.OptionUserscrd = customtkinter.CTkButton(master=self, text="Usuarios", command=lambda: self.sendNotification("Usuarios"))
        self.OptionUserscrd.grid(row=0, column=0, padx=10, pady=(10, 5))
        self.OptionPacientesscrd = customtkinter.CTkButton(master=self, text="Pacientes", command=lambda: self.sendNotification("Pacientes"))
        self.OptionPacientesscrd.grid(row=1, column=0, padx=10, pady=(5, 5))
        self.OptionDatesscrd = customtkinter.CTkButton(master=self, text="Citas", command=lambda: self.sendNotification("Citas"))
        self.OptionDatesscrd.grid(row=2, column=0, padx=10, pady=(5, 5))
        self.OptionDisease = customtkinter.CTkButton(master=self, text="Enfermedades", command=lambda: self.sendNotification("Enfermedades"))
        self.OptionDisease.grid(row=3, column=0, padx=10, pady=(5, 5))
        self.OptionSign = customtkinter.CTkButton(master=self, text="Signos", command=lambda: self.sendNotification("Signos"))
        self.OptionSign.grid(row=4, column=0, padx=10, pady=(5, 5))
        self.OptionSymptoms = customtkinter.CTkButton(master=self, text="Sintomas", command=lambda: self.sendNotification("Sintomas"))
        self.OptionSymptoms.grid(row=5, column=0, padx=10, pady=(5, 5))
        self.OptionSettings = customtkinter.CTkButton(master=self, text="Salir", command=lambda: self.sendNotification("Exit"))
        self.OptionSettings.grid(row=6, column=0, padx=10, pady=(5, 5))
        
    def sendNotification(self,message):
        self.master.updateCrud(message)