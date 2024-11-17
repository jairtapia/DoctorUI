import customtkinter as ctk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from controller.DiagnosticController import DiagnosticController

class DataPatient(ctk.CTk):
    def __init__(self, paciente, **kwargs):
        super().__init__(**kwargs)
        self.controller = DiagnosticController()
        self.pacienteid = paciente
        print(self.controller.GetHistorical(self.pacienteid))
        self.configure(fg_color='#82a5b9', corner_radius=15, width=800, height=500)
        # Crear el frame con scroll
        self.scroll_frame = ctk.CTkScrollableFrame(self, fg_color='#82a5b9', width=800, height=500, corner_radius=15)
        self.scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)  # Expandir para que ocupe toda la ventana
        # Usaremos grid en lugar de place
        self.scroll_frame.grid_columnconfigure(0, weight=1)
        self.scroll_frame.grid_columnconfigure(1, weight=1)
        dfApi = pd.DataFrame(self.controller.GetHistorical(self.pacienteid))
        dfApi['estado'] = dfApi['estado'].astype(int)
        dfApi['fecha'] = pd.to_datetime(dfApi['fecha'])
        df_sorted = dfApi.sort_values(by="fecha")
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.fill_between(df_sorted['fecha'], df_sorted['estado'], color='skyblue')
        ax.set_xlabel("Estado")
        ax.set_ylabel("Fecha")
        ax.set_title("historial de salud del paciente")
        canvas = FigureCanvasTkAgg(fig, master=self.scroll_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side="top", fill="both", expand=True)


