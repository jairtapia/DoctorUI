import customtkinter
from Frames.Login.login import login
from Frames.Register.register import register
from assets.themes.AdminPalette import AdminTheme

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("900x600")  # Tamaño de la ventana principal
        self.title("Loggin")
        self.configure(fg_color=AdminTheme['background'])
        self.currentCard = None
        self.switchButtonTextContent = 'registrarse'
        self.setSwitchButton()
        self.setCardLogin()
        self.showCurrentCard()
        
    def showCurrentCard(self):
        self.currentCard.place(relx=0.5, rely=0.5, anchor="center")

    def toggleCard(self):
        if isinstance(self.currentCard, login):
            self.currentCard.destroy() 
            self.switchButtonTextContent = 'Entrar'
            self.setCadrRegister()
        elif isinstance(self.currentCard,register):
            self.currentCard.destroy()
            self.switchButtonTextContent = 'Registrarse'
            self.setCardLogin()
        self.SwitchButton.configure(text=self.switchButtonTextContent)
        self.showCurrentCard()

    def setSwitchButton(self):
        self.SwitchButton = customtkinter.CTkButton(master= self,text=self.switchButtonTextContent, command=self.toggleCard)
        self.SwitchButton.configure(fg_color=AdminTheme['new'])
        self.SwitchButton.grid(row=1, column=1, padx=10, pady=10)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def setCardLogin(self):
        self.currentCard = login(master=self)

    def setCadrRegister(self):
        self.currentCard = register(master=self)
    

if __name__ == "__main__":
    app = App()
    app.mainloop()