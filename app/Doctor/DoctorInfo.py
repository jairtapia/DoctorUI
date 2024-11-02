import customtkinter
class info(customtkinter.CTkFrame):
    def __init__(self, master,id, **kwargs):
        self.id = id
        super().__init__(master, **kwargs)
        self.configure(fg_color="#d9d9d9", corner_radius=15, width=880, height=150)
        