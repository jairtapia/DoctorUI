import customtkinter

class Utils(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="#d9d9d9", corner_radius=15, width=500, height=50)
        self.setInputs()

    def setInputs(self):
        self.SearchInput = customtkinter.CTkEntry(master=self, placeholder_text="Search", text_color="black", width=230)
        self.SearchInput.configure(fg_color="white", border_color="white")
        self.SearchInput.grid(row=0, column=0, padx=(10, 2), pady=10, sticky="w")
        self.searchButton = customtkinter.CTkButton(self, text='find', command=self.search)
        self.searchButton.grid(row=0, column=1, padx=(2, 2), pady=10, sticky="w")
        self.CreateButton = customtkinter.CTkButton(self, text='Nuevo', command=self.openModal)
        self.CreateButton.grid(row=0, column=2, padx=(2, 10), pady=10, sticky="w")

    def search(self):
        self.master.search()

    def openModal(self):
        self.master.openModal()