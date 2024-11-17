import customtkinter as ctk
from tkinter import messagebox
from controller.SymptomController import SymptomController
from assets.themes.AdminPalette import AdminTheme
from Frames.Box.DynamicBox import Box

class TestModal(ctk.CTkToplevel):
    def __init__(self, master,id, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.controller = SymptomController()
        self.Disease = id
        self.dataPrueba = [{"id":1,"name":"prueba de sangre"},{"id":2,"name":"nose"}]
        self.selected = [{"id":2,"name":"nose"}]#buscar las pruebas de laboratorio de acuerto al id
        self.InitData()

    def InitData(self):
        self.TestsBox = Box(master=self, text='pruebas', selected=self.selected, data=self.dataPrueba)

