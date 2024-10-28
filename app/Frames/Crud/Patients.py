import customtkinter

class PatientsCrud(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="#d9d9d9", corner_radius=15, width=500, height=550)
        self.label = customtkinter.CTkLabel(master=self, text="Patients Crud", text_color="black", font=("Arial", 20))
        self.label.place(x=10,y=10)

    def setInputs(self):
        pass


if __name__ =="__main__":
    class App(customtkinter.CTk):
        def __init__(self):
            super().__init__()
            self.geometry("900x600")  # Tamaño de la ventana principal
            self.title("test Frame")
            self.frame = PatientsCrud(master=self)
            self.frame.grid(row=0, column=1, sticky="nsew",pady = 10,padx=5)
        
    app = App()
    app.mainloop() 