import customtkinter
from assets.themes.AdminPalette import AdminTheme
class appointments(customtkinter.CTkFrame):
    def __init__(self, master, id,**kwargs):
        super().__init__(master, **kwargs)
        self.id = id
        self.configure(fg_color=AdminTheme['tertiary'], corner_radius=15, width=900, height=300)
        self.grid_rowconfigure(0, weight=1)  # Permitir que la fila 0 se expanda
        self.grid_columnconfigure(0, weight=1)
        print(self.id)