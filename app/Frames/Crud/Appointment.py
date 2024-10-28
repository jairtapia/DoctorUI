import customtkinter

class AppointmentCrud(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="#d9d9d9", corner_radius=15, width=500, height=550)
        self.label = customtkinter.CTkLabel(master=self, text="Citas Crud", text_color="black", font=("Arial", 20))
        self.label.place(x=10,y=10)

    def setInputs(self):
        pass