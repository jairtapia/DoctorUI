import customtkinter
from assets.themes.AdminPalette import AdminTheme
from controller.AppointmentController import appointmentController
class appointments(customtkinter.CTkScrollableFrame):
    def __init__(self, master, id,**kwargs):
        super().__init__(master, **kwargs)
        self.MyController = appointmentController()
        self.id = id
        self.configure(fg_color=AdminTheme['tertiary'], corner_radius=15, width=900, height=300)
        self.grid_rowconfigure(0, weight=1)  # Permitir que la fila 0 se expanda
        self.grid_columnconfigure(0, weight=1)
        print(self.id)
        self.getAppointments()

    def getAppointments(self):
        content = self.MyController.getAppointmentsByDoctor(self.id)
        print(content)  # Imprimir contenido para depuración

        # Limpiar tarjetas previas si existían
        for widget in self.winfo_children():
            widget.destroy()

        if not content:
            customtkinter.CTkLabel(self, text="No se encontraron citas.").pack(pady=10)
            return

        # Crear una tarjeta para cada cita
        for appointment in content:
            self.create_appointment_card(appointment)

    def create_appointment_card(self, appointment):
        # Crear un Frame para cada tarjeta de cita dentro del scrollable frame
        card = customtkinter.CTkFrame(self, corner_radius=10, fg_color="white", border_color="gray", border_width=1)
        card.pack(fill="x", padx=10, pady=5)
        # Agregar detalles de la cita a la tarjeta
        customtkinter.CTkLabel(card, text=f"Fecha: {appointment['date']}", text_color="black").pack(anchor="w", padx=10, pady=2)
        customtkinter.CTkLabel(card, text=f"Hora: {appointment['time']}", text_color="black").pack(anchor="w", padx=10, pady=2)
        customtkinter.CTkLabel(card, text=f"Doctor ID: {appointment['doctor_id']}", text_color="black").pack(anchor="w", padx=10, pady=2)
        customtkinter.CTkLabel(card, text=f"Paciente: {appointment['patient']['name']} {appointment['patient']['lastname']}", text_color="black").pack(anchor="w", padx=10, pady=2)
        customtkinter.CTkLabel(card, text=f"Sala: {appointment['clinic_room']['numero']}", text_color="black").pack(anchor="w", padx=10, pady=2)
