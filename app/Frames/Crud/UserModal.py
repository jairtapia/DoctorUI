
import customtkinter

class UserModal(customtkinter.CTkToplevel):
    def __init__(self, master,id=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="#d9d9d9", corner_radius=15, width=400, height=450)
        self.id = id
        print(self.id)
        if self.id is None:
            self.title = "nuevo usuario"
            self.buttonSend = customtkinter.CTkButton(master=self,text="guardar",command=self.CreateNew)
        self.buttonSend = customtkinter.CTkButton(master=self,text="guardar",command=self.EditUser)
        self.Tittle = "editar Usuario"
        self.label = customtkinter.CTkLabel(master=self, text=self.Tittle, text_color="black", font=("Arial", 20))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.buttonSend.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        

    def CreateNew(self):
        print("creando uno nuevo")
        self.destroy()

    def EditUser(self):
        print(f'editando usuario {self.id}')
        self.destroy()