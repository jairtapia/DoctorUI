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
        
    def sendNotification(self,message):
        self.master.updateCrud(message)
    
    

if __name__ =="__main__":
    class App(customtkinter.CTk):
        def __init__(self):
            super().__init__()
            self.geometry("900x600")  # Tamaño de la ventana principal
            self.title("test Frame")
            self.frame = navigator(master=self)
            self.frame.grid(row=0, column=0, sticky="nsew",pady = 10,padx=5)

        def updateCrud(self, message):
            print(message)
        
    app = App()
    app.mainloop()        