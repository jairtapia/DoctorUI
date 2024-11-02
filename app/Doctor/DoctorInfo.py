import customtkinter
from controller.UserController import UserController
class info(customtkinter.CTkFrame):
    def __init__(self, master,id, **kwargs):
        self.controller = UserController()
        self.id = id
        super().__init__(master, **kwargs)
        self.configure(fg_color="#d9d9d9", corner_radius=15, width=880, height=150)
        self.Tittle = customtkinter.CTkLabel(master=self,text='Medico',text_color="black")
        self.labelName = customtkinter.CTkLabel(master=self,text='unknown',text_color="black")
        self.labelLastName_f = customtkinter.CTkLabel(master=self,text='unknown',text_color="black")
        self.labelLastName_m = customtkinter.CTkLabel(master=self,text='unknown',text_color="black")
        self.labelPhone = customtkinter.CTkLabel(master=self,text='unknown',text_color="black")
        #self.buttonNew = customtkinter.CTkButton(master=self,text="nuevo",command=self.addNew)
        self.getInfo()
        self.setText()
        #self.buttonNew.grid(row=1, column=1, padx=10, pady=5, sticky="e")  # Botón alineado a la derecha

    def addNew(self):
        print('hicealgo')

    def setText(self):
        self.labelName.grid(row=0, column=0, padx=10, pady=5, sticky="w")  # Alinear a la izquierda
        self.labelLastName_f.grid(row=1, column=0, padx=10, pady=5, sticky="w")  # Alinear a la izquierda
        self.labelLastName_m.grid(row=2, column=0, padx=10, pady=5, sticky="w")  # Alinear a la izquierda
        self.labelPhone.grid(row=3, column=0, padx=10, pady=5, sticky="w")  # Alinear a la izquierda

    def getInfo(self):
        self.user = self.controller.findById(self.id)
        if self.user:
            self.loadInfo()
    
    def loadInfo(self):
        self.labelName.configure(text=self.user['user_name'])
        self.labelLastName_f.configure(text=self.user['last_name_f'])
        self.labelLastName_m.configure(text=self.user['last_name_m'])
        self.labelPhone.configure(text=self.user['telefono'])
