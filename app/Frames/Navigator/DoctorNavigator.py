import customtkinter
from Frames.DoctorList.Appointments import appointments
from assets.themes.AdminPalette import AdminTheme
from Frames.DoctorList.PatientsList import Patients

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
        self.currentCard = appointments(master=self, id = self.id)
        self.showCard()
        
    def showCard(self):
        self.currentCard.grid(row=1, column=0, padx=10, pady=5)
    
    def setButtons(self):
        self.buttonContainer.configure(fg_color=AdminTheme['primary'], corner_radius=15, width=700, height=50)
        self.buttonappointments  = customtkinter.CTkButton(master=self.buttonContainer, text='Citas', command=lambda: self.SwitchCard('Citas'))
        self.buttonPatients  = customtkinter.CTkButton(master=self.buttonContainer, text='Pacientes', command=lambda: self.SwitchCard('Pacientes'))
        self.buttonNew  = customtkinter.CTkButton(master=self.buttonContainer, text='Nuevo', command=lambda: self.SwitchCard('Nuevo'))
        self.buttonappointments.grid(row=0, column=0, padx=10, pady=5) 
        self.buttonPatients.grid(row=0, column=1, padx=10, pady=5)
        self.buttonNew.grid(row=0, column=2, padx=10, pady=5)

    def SwitchCard(self,topic):
        self.currentCard.destroy()
        if topic == 'Pacientes':
            self.currentCard = Patients(master=self,id = self.id)
        elif topic == 'Citas':
            self.currentCard = appointments(master=self, id = self.id)
        else:
            if isinstance(self.currentCard,appointments):
                print('creando nueva cita')
            else:
                print('creando paciente')
        self.showCard()

