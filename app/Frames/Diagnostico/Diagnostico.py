import customtkinter as ctk
from datetime import date
from Frames.Box.DynamicBox import Box
from controller.SymptomController import SymptomController
from controller.SignController import SignController
from Frames.Crud.Modal.Tests import TestModal
from dto.Diagnostic import DiagnosticDto
from controller.DiagnosticController import DiagnosticController
from controller.DiseaseController import DiseaseController
from tkinter import messagebox
from Frames.Diagnostico.motor import MotorDeInferenciaIncremental

class Diagnostico(ctk.CTk):
    def __init__(self, Medico, paciente,fecha,**kwargs):
        super().__init__(**kwargs)
        self.controller = DiagnosticController()
        self.date = fecha
        self.medicoid = Medico
        self.pacienteid = paciente
        self.controllerSymptoms = SymptomController()
        self.controllerSigns = SignController()
        self.controllerDisease = DiseaseController()
        self.ProbDiseases = None
        self.motor_inferencia = MotorDeInferenciaIncremental()
        #Configuración de la ventana
        self.configure(fg_color='#82a5b9', corner_radius=15, width=500, height=600)
        # Crear el frame con scroll
        self.scroll_frame = ctk.CTkScrollableFrame(self, fg_color='#82a5b9', width=500, height=600, corner_radius=15)
        self.scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)  # Expandir para que ocupe toda la ventana
        # Usaremos grid en lugar de place
        self.scroll_frame.grid_columnconfigure(0, weight=1)
        self.scroll_frame.grid_columnconfigure(1, weight=1)
        # Widgets organizados con grid
        self.label = ctk.CTkLabel(self.scroll_frame, text="Diagnostico", font=("Arial", 18), text_color="white")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)
        self.descripcion = ctk.CTkEntry(self.scroll_frame, placeholder_text="Descripción", width=400, text_color='black')
        self.descripcion.configure(fg_color="white", border_color="white")
        self.descripcion.grid(row=1, column=0, columnspan=2, pady=5, padx=10)
        self.receta = ctk.CTkEntry(self.scroll_frame, placeholder_text="Receta", width=400, text_color='black')
        self.receta.configure(fg_color="white", border_color="white")
        self.receta.grid(row=2, column=0, columnspan=2, pady=5, padx=10)
        self.SymptomsBox = Box(master=self.scroll_frame, text='Síntomas', selected=None, data=self.controllerSymptoms.get_symptoms())
        self.SymptomsBox.grid(row=3, column=0, pady=10, padx=10)
        self.SingsBox = Box(master=self.scroll_frame, text='Signos', selected=None, data=self.controllerSigns.GetSigns())
        self.SingsBox.grid(row=3, column=1, pady=10, padx=10)
        self.DiseaseBox = Box(master=self.scroll_frame, text='Enfermedades', selected=None, data=self.ProbDiseases)
        self.DiseaseBox.grid(row=4, column=0, columnspan=2, pady=10, padx=10)
        self.boton_generar = ctk.CTkButton(self.scroll_frame, text="Predecir", command=self.Predecir)
        self.boton_generar.grid(row=5, column=0, pady=10)
        self.analisis = ctk.CTkButton(self.scroll_frame, text="analisis de laboratorio", command=self.verAnalisis)
        self.analisis.grid(row=5, column=1, pady=10, padx=10)
        self.estado = ctk.CTkEntry(self.scroll_frame, placeholder_text="Estado", width=400, text_color='black', fg_color="white", border_color="white")
        self.estado.grid(row=6, column=0, columnspan=2, pady=10, padx=10)
        self.boton_guardar = ctk.CTkButton(self.scroll_frame, text="Guardar", command=self.guardar)
        self.boton_guardar.grid(row=7, column=0, columnspan=2, pady=10)

    def updateDiseases(self):
        if hasattr(self, 'DiseaseBox'):
            self.DiseaseBox.grid_forget()
            self.DiseaseBox.destroy()
        # Mostrar enfermedades con probabilidad formateada
        self.DiseaseBox = Box(master=self.scroll_frame, text='Enfermedades', selected=None, data=self.ProbDiseases)
        self.DiseaseBox.grid(row=4, column=0, columnspan=2, pady=10, padx=10)

    def guardar(self):
        try:
            medico = self.medicoid
            paciente = self.pacienteid
            fecha = self.date
            descripcion = self.descripcion.get()
            receta = self.receta.get()
            name = self.DiseaseBox.getValueNames()
            nombre = name[0]
            enfermedad = self.controllerDisease.findByName(nombre)['id']
            estado = self.estado.get()
            diagnostico = DiagnosticDto(
                medico=medico,
                paciente=paciente,
                fecha=fecha,
                descripcion=descripcion,
                receta=receta,
                enfermedad=enfermedad,
                estado=estado
                )
            iddg = self.controller.CreateDiagnostic(diagnostico)['id']
            if iddg:
                if self.controller.UpdateHistorical(iddg,paciente):
                    messagebox.showinfo("Guardado", "El registro se ha guardado correctamente.")

        except Exception as e:
            messagebox.showerror("Error", f"Unknown error: {e}")

    def verAnalisis(self):
        nombre = self.DiseaseBox.getValueNames()[0]
        enfermedad = self.controllerDisease.findByName(nombre)['id']
        self.modal = TestModal(master=self, id=enfermedad)
        self.modal.protocol("WM_DELETE_WINDOW", self.destroyModal)
        self.modal.grab_set()  # Para evitar interacción con otras ventanas
        self.modal.lift()  # Elevar la ventana modal
        self.modal.focus_set()

    def destroyModal(self):
        self.modal.destroy()
        self.modal = None

    def Predecir(self):
        """
        Realiza la predicción de enfermedades con base en los signos y síntomas seleccionados.
        """

        # Comprobar que no existan nuevas enfermedades
        self.motor_inferencia.sincronizar_enfermedades()

        # Obtener signos y síntomas seleccionados
        signos = self.SingsBox.getValueNames()
        sintomas = self.SymptomsBox.getValueNames()

        # Imprimir los valores de signos y síntomas para depuración
        print("Signos seleccionados:", signos)
        print("Síntomas seleccionados:", sintomas)

        # Validar que se hayan proporcionado signos y síntomas
        if not signos and not sintomas:
            messagebox.showerror("Error", "Ingrese algún síntoma o signo.")
            return  # Salir de la función si la validación falla

        # Usar el motor de inferencia para predecir
        try:
            resultados = self.motor_inferencia.predecir(signos, sintomas)
            print("Resultados de la predicción:", resultados)  # Para depuración

            # Actualizar enfermedades probables en la interfaz
            self.ProbDiseases = [{"name": r[0], "confidence": f"{r[1]:.2f}%"} for r in resultados]
            self.updateDiseases()

        except Exception as e:
            # Manejar cualquier error inesperado durante la predicción
            print(f"Error durante la predicción: {e}")
            messagebox.showerror("Error", "Ocurrió un error durante la predicción. Por favor, intente nuevamente.")
