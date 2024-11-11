import customtkinter as ctk
from assets.themes.AdminPalette import AdminTheme
from controller.PatientController import PatientController
from dto.Patient import PatientDto
from tkinter import messagebox

class PatientForm(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.controller = PatientController()
        self.configure(fg_color=AdminTheme['tertiary'], width=880, height=350)
        self.create_widgets()

    def create_widgets(self):
        label_title = ctk.CTkLabel(self, text="Formulario de paciente", font=("Arial", 16),text_color='black')
        label_title.pack(pady=10)
        frame_search = ctk.CTkFrame(self, fg_color=AdminTheme['tertiary'])
        frame_search.pack(pady=10)
        self.inputSearch = ctk.CTkEntry(frame_search, placeholder_text="Search", text_color='black', width=500, fg_color='white')
        self.inputSearch.pack(side='left')
        buttonSearch = ctk.CTkButton(frame_search, text="buscar",command=self.setData)
        buttonSearch.pack(side='left', padx=5)
        formFrame = ctk.CTkFrame(self, fg_color=AdminTheme['tertiary'])
        frame_left = ctk.CTkFrame(formFrame, fg_color=AdminTheme['tertiary'])
        frame_left.grid(row=0, column=0, padx=10, pady=5)

        self.name = ctk.CTkEntry(frame_left, placeholder_text="Nombre", width=150, text_color='black')
        self.name.configure(fg_color="white", border_color="white")
        self.name.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.firstName = ctk.CTkEntry(frame_left, placeholder_text="Apellido paterno", width=150, text_color='black')
        self.firstName.configure(fg_color="white", border_color="white")
        self.firstName.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.SecondName = ctk.CTkEntry(frame_left, placeholder_text="Apellido materno", width=150, text_color='black')
        self.SecondName.configure(fg_color="white", border_color="white")
        self.SecondName.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.age = ctk.CTkEntry(frame_left, placeholder_text="Edad", width=150, text_color='black')
        self.age.configure(fg_color="white", border_color="white")
        self.age.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

        frame_right = ctk.CTkFrame(formFrame, fg_color=AdminTheme['tertiary'])
        frame_right.grid(row=0, column=1, padx=10, pady=5)

        self.phone = ctk.CTkEntry(frame_right, placeholder_text="Teléfono", width=150, text_color='black')
        self.phone.configure(fg_color="white", border_color="white")
        self.phone.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.address = ctk.CTkEntry(frame_right, placeholder_text="Dirección", width=150, text_color='black')
        self.address.configure(fg_color="white", border_color="white")
        self.address.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.state = ctk.CTkEntry(frame_right, placeholder_text="Estado", width=150, text_color='black')
        self.state.configure(fg_color="white", border_color="white")
        self.state.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        formFrame.pack(pady=10)
        OptionFrame = ctk.CTkFrame(self, fg_color=AdminTheme['tertiary'])  
        buttonCreate = ctk.CTkButton(OptionFrame, text="Crear",command=self.enviar_datos)
        buttonCreate.pack(side='left', padx=5)  
        buttonEdit = ctk.CTkButton(OptionFrame, text="Editar",command=self.edit)
        buttonEdit.pack(side='left', padx=5)    
        buttonDelete = ctk.CTkButton(OptionFrame, text="Eliminar",command=self.delete)
        buttonDelete.pack(side='left', padx=5) 
        OptionFrame.pack(pady=10)

    def enviar_datos(self):
        try:
            patient = PatientDto( 
                name=self.name.get(),
                last_name_f=self.firstName.get(),  # Asegúrate de que esta propiedad esté en el formulario
                last_name_m=self.SecondName.get(),  # Asegúrate de que esta propiedad esté en el formulario
                age=int(self.age.get()),  # Asegúrate de que la edad sea un número entero
                phone=self.phone.get(),
                address=self.address.get(),  # Agrega el campo de dirección
                state=self.state.get()  # Agrega el campo de estado
            )
            print(patient)
            result = self.controller.CreatePatient(patient)
            if result:
                messagebox.showinfo("Éxito", "Paciente guardado correctamente.")
            else:
                messagebox.showerror("Error", "No se pudo guardar el paciente.")
        except Exception as e:
                messagebox.showerror("Error", "no se creo el paciente")
    
    def edit(self):
        self.PatientId = self.inputSearch.get()
        try:
            patient = PatientDto( 
                name=self.name.get(),
                last_name_f=self.firstName.get(),
                last_name_m=self.SecondName.get(),
                age=int(self.age.get()),
                phone=self.phone.get(),
                address=self.address.get(),
                state=self.state.get()
            )
            result = self.controller.EditPatient(patient,self.PatientId)
            if result:
                messagebox.showinfo("Éxito", "Paciente actualizado correctamente.")
            else:
                messagebox.showerror("Error", "No se pudo actualizar el paciente.")
        except Exception as e:
                messagebox.showerror("Error", f"Error al crear la de modal cita: {e}")

    def setData(self):
        try:
            try:
                self.PatientId = self.inputSearch.get()
            except Exception as e:
                messagebox.showerror("Error", f"Error al obtener el ID de la cita: {e}")
            pass
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener los datos: {e}")

    def delete(self):
        try:
            self.PatientId = self.inputSearch.get()
            confirmation = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas eliminar este paciente?")
            if confirmation:
                result = self.controller.Delete(self.PatientId)
                if result:
                    messagebox.showinfo("Éxito", "Paciente eliminado correctamente.")
                else:
                    messagebox.showerror("Error", "No se pudo eliminar el paciente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener el ID de la cita: {e}")

