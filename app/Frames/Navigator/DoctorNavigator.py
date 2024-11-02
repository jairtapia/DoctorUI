import customtkinter
from Frames.DoctorList.Appointments import appointments
from assets.themes.AdminPalette import AdminTheme

class navigator(customtkinter.CTkFrame):
    def __init__(self, master, id,**kwargs):
        super().__init__(master, **kwargs)
        self.id = id
        self.grid_rowconfigure(0, weight=1)  # Permitir que la fila 0 se expanda
        self.grid_rowconfigure(1, weight=1)  # Permitir que la fila 1 se expanda
        self.grid_columnconfigure(0, weight=1) 
        self.configure(fg_color="#d9d9d9", corner_radius=15, width=880, height=350)
        self.buttonContainer = customtkinter.CTkFrame(master=self)
        self.setButtons()
        self.buttonContainer.grid(row=0, column=0, padx=10, pady=5)
        self.appointmenstCard = appointments(master=self, id = self.id)
        self.appointmenstCard.grid(row=1, column=0, padx=10, pady=5)
    
    def setButtons(self):
        self.buttonContainer.configure(fg_color=AdminTheme['primary'], corner_radius=15, width=700, height=50)
        self.buttonappointments  = customtkinter.CTkButton(master=self.buttonContainer,text='Citas')
        self.buttonPatients  = customtkinter.CTkButton(master=self.buttonContainer,text='Pacientes')
        self.buttonappointments.grid(row=0, column=0, padx=10, pady=5) 
        self.buttonPatients.grid(row=0, column=1, padx=10, pady=5)