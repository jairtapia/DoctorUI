import json
import requests
import numpy as np
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import MultiLabelBinarizer

class MotorDeInferenciaIncremental:
    def __init__(self):
        # Endpoint de la API
        self.api_endpoint = "http://127.0.0.1:8000/createModel"

        # Cargar los datos desde el archivo JSON
        self.archivo_json = "app/Frames/Diagnostico/datos_enfermedades.json"
        self.signos_y_sintomas = self.cargar_datos()

        # Sincronizar enfermedades con la API
        self.sincronizar_enfermedades()

        # Lista de todas las enfermedades
        self.enfermedades = [enfermedad['nombre'] for enfermedad in self.signos_y_sintomas]

        # Codificación de síntomas/signos
        self.ml_binarizer = MultiLabelBinarizer()
        self.x_data, self.y_data = self.preparar_datos(self.signos_y_sintomas)

        # Crear el clasificador incremental (SGD)
        self.modelo = SGDClassifier(loss="log_loss", max_iter=1000, tol=1e-3)

        # Entrenamiento inicial
        self.modelo.fit(self.x_data, self.y_data)

    def cargar_datos(self):
        """
        Cargar los datos de enfermedades y síntomas desde un archivo JSON.
        """
        try:
            with open(self.archivo_json, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def guardar_datos(self):
        """
        Guardar los datos actualizados de enfermedades y síntomas en el archivo JSON.
        """
        with open(self.archivo_json, 'w') as file:
            json.dump(self.signos_y_sintomas, file, indent=4)

    def sincronizar_enfermedades(self):
        """
        Sincronizar las enfermedades locales con las proporcionadas por el endpoint de la API.
        El archivo JSON solo se actualiza si hay nuevas enfermedades o cambios.
        """
        try:
            response = requests.get(self.api_endpoint)
            if response.status_code == 200:
                enfermedades_api = response.json()  # Asume que el endpoint devuelve un JSON
                enfermedades_local = {enf['nombre']: enf for enf in self.signos_y_sintomas}

                # Revisar enfermedades desde la API
                nuevas_enfermedades = []
                for enfermedad in enfermedades_api:
                    nombre = enfermedad['nombre']
                    sintomas = set(enfermedad['sintomas'])

                    # Evitar duplicados: verificar si ya existe con los mismos datos
                    if nombre not in enfermedades_local or set(enfermedades_local[nombre]['sintomas']) != sintomas:
                        nuevas_enfermedades.append(enfermedad)

                if nuevas_enfermedades:
                    print(f"Se encontraron {len(nuevas_enfermedades)} nuevas enfermedades. Actualizando JSON...")
                    self.signos_y_sintomas.extend(nuevas_enfermedades)
                    self.guardar_datos()  # Guardar solo si hay cambios
                else:
                    print("No se encontraron nuevas enfermedades.")
            else:
                print(f"Error al consultar la API. Código de estado: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error al conectar con la API: {e}")


    def agregar_enfermedad(self, nombre, sintomas):
        """
        Agregar una nueva enfermedad y sus síntomas al archivo JSON.
        """
        # Agregar la nueva enfermedad a la lista de signos y síntomas
        self.signos_y_sintomas.append({"nombre": nombre, "sintomas": sintomas})

        # Guardar los datos en el archivo JSON
        self.guardar_datos()

        # Actualizar el modelo con la nueva enfermedad
        self.actualizar_modelo(sintomas, nombre)

    def preparar_datos(self, signos_y_sintomas):
        """
        Convertir los datos de los signos y síntomas a una matriz de características (one-hot encoding)
        """
        sintomas_unicos = set()
        for enfermedad in signos_y_sintomas:
            sintomas_unicos.update(enfermedad['sintomas'])

        sintomas_unicos = list(sintomas_unicos)
        x_data = []
        y_data = []

        for enfermedad in signos_y_sintomas:
            sintomas = enfermedad['sintomas']
            x_data.append([1 if sintoma in sintomas else 0 for sintoma in sintomas_unicos])
            y_data.append(enfermedad['nombre'])

        return np.array(x_data), np.array(y_data)

    def predecir(self, signos, sintomas):
        """
        Recibe dos listas: signos y sintomas. Devuelve las 5 enfermedades más probables con su porcentaje de acierto.
        """
        sintomas_unicos = set()
        for enfermedad in self.signos_y_sintomas:
            sintomas_unicos.update(enfermedad['sintomas'])
        sintomas_unicos = list(sintomas_unicos)

        # Crear la representación binaria para los signos y síntomas proporcionados
        input_data = [1 if sintoma in signos + sintomas else 0 for sintoma in sintomas_unicos]

        # Predecir las probabilidades para cada enfermedad
        probabilidades = self.modelo.predict_proba([input_data])[0]

        # Emparejar las probabilidades con los nombres de las enfermedades
        resultados = [(self.enfermedades[i], probabilidades[i] * 100) for i in range(len(probabilidades))]

        # Ordenar por probabilidad y devolver las 5 enfermedades más probables
        resultados_ordenados = sorted(resultados, key=lambda x: x[1], reverse=True)[:10]

        return resultados_ordenados

    def actualizar_modelo(self, nuevos_signos, nueva_enfermedad):
        """
        Recibe nuevos signos y síntomas, y la enfermedad asociada.
        Actualiza el modelo de inferencia con estos nuevos datos.
        """
        # Preparar los nuevos datos
        sintomas_unicos = set()
        for enfermedad in self.signos_y_sintomas:
            sintomas_unicos.update(enfermedad['sintomas'])
        sintomas_unicos = list(sintomas_unicos)

        input_data = [1 if sintoma in nuevos_signos else 0 for sintoma in sintomas_unicos]

        # Añadir los nuevos datos a la lista
        self.x_data = np.append(self.x_data, [input_data], axis=0)
        self.y_data = np.append(self.y_data, [nueva_enfermedad], axis=0)

        # Actualizar el modelo con los nuevos datos
        self.modelo.partial_fit(self.x_data, self.y_data, classes=np.unique(self.y_data))



'''
# Ejemplo de uso
motor = MotorDeInferenciaIncremental()

# Nuevos signos y síntomas que queremos agregar
signos_nuevos = ["Cianosis", "Tos persistente"]
sintomas_nuevos = ["Fatiga", "Dificultad para respirar"]

# Predecir las enfermedades más probables con los datos existentes
resultados_iniciales = motor.predecir(signos_nuevos, sintomas_nuevos)
print("Resultados iniciales:", resultados_iniciales)

# Si el motor no tiene la enfermedad, agregarla al modelo (aprendizaje incremental)
nueva_enfermedad = "EPOC"
motor.agregar_enfermedad(nueva_enfermedad, signos_nuevos + sintomas_nuevos)

# Volver a predecir después de la actualización
resultados_actualizados = motor.predecir(signos_nuevos, sintomas_nuevos)
print("Resultados actualizados:", resultados_actualizados)

'''
