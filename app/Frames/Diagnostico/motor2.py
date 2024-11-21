import json
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import MultiLabelBinarizer
import numpy as np

class MotorDeInferenciaIncrementala:
    def __init__(self):
        self.archivo_json = "/home/daniel-guillen/Documentos/Proyecto_diagnostico/good-version/DoctorUI/app/Frames/Diagnostico/signos_y_sintomas.json"
        self.cargar_datos()

        # Codificación de síntomas/signos
        self.ml_binarizer = MultiLabelBinarizer()
        self.x_data, self.y_data = self.preparar_datos(self.datos_enfermedades)


        self.modelo = SGDClassifier(loss='log_loss')


        # Entrenamiento inicial
        self.modelo.fit(self.x_data, self.y_data)

    def cargar_datos(self):
        """Cargar los datos desde el archivo JSON."""
        with open(self.archivo_json, 'r') as file:
            self.datos_enfermedades = json.load(file)

        # Lista de todas las enfermedades
        self.enfermedades = [enfermedad["nombre"] for enfermedad in self.datos_enfermedades]

    def preparar_datos(self, datos):
        """Convertir los datos a una matriz de características (one-hot encoding)."""
        sintomas_unicos = set(sintoma for enfermedad in datos for sintoma in enfermedad["sintomas"])
        sintomas_unicos = list(sintomas_unicos)

        x_data = []
        y_data = []

        for enfermedad in datos:
            x_data.append([1 if sintoma in enfermedad["sintomas"] else 0 for sintoma in sintomas_unicos])
            y_data.append(enfermedad["nombre"])

        return np.array(x_data), np.array(y_data)

    def predecir(self, signos, sintomas):
        """Predecir las enfermedades más probables."""
        sintomas_unicos = set(sintoma for enfermedad in self.datos_enfermedades for sintoma in enfermedad["sintomas"])
        sintomas_unicos = list(sintomas_unicos)

        input_data = [1 if sintoma in signos + sintomas else 0 for sintoma in sintomas_unicos]
        probabilidades = self.modelo.predict_proba([input_data])[0]

        resultados = [(self.enfermedades[i], probabilidades[i] * 100) for i in range(len(self.enfermedades))]
        resultados_ordenados = sorted(resultados, key=lambda x: x[1], reverse=True)[:5]
        return [{"name": nombre, "confidence": probabilidad} for nombre, probabilidad in resultados_ordenados]


    def actualizar_modelo(self, nuevos_signos, nueva_enfermedad):
        """Actualiza el modelo con nuevos signos, síntomas y enfermedad."""
        # Añadir los nuevos signos y síntomas al archivo JSON
        self.signos_y_sintomas.append({nueva_enfermedad: nuevos_signos})
        self.guardar_datos()

        # Preparar los nuevos datos
        sintomas_unicos = set()
        for enfermedad in self.signos_y_sintomas:
            for sintomas in enfermedad.values():
                sintomas_unicos.update(sintomas)
        sintomas_unicos = list(sintomas_unicos)

        input_data = [1 if sintoma in nuevos_signos else 0 for sintoma in sintomas_unicos]

        # Añadir los nuevos datos a la lista
        self.x_data = np.append(self.x_data, [input_data], axis=0)
        self.y_data = np.append(self.y_data, [nueva_enfermedad], axis=0)

        # Actualizar el modelo con aprendizaje incremental
        self.modelo.partial_fit(self.x_data, self.y_data, classes=np.unique(self.y_data))

'''
# Crear una instancia del motor
motor = MotorDeInferenciaIncremental("signos_y_sintomas.json")

# Predecir enfermedades basadas en signos y síntomas
signos_nuevos = ["Cianosis", "Tos persistente"]
sintomas_nuevos = ["Fatiga", "Dificultad para respirar"]
resultados = motor.predecir(signos_nuevos, sintomas_nuevos)
print("Resultados:", resultados)

# Actualizar el modelo con una nueva enfermedad
nueva_enfermedad = "Enfermedad X"
nuevos_signos = ["Fiebre", "Dolor de cabeza"]
motor.actualizar_modelo(nuevos_signos, nueva_enfermedad)
print(f"Modelo actualizado con la enfermedad: {nueva_enfermedad}")

'''
