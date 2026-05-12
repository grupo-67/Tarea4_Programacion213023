#importamos los comportamiento heredados de la clase padre Servicio
from models.servicio import Servicio


class ServicioAsesoria(Servicio):

    def __init__(self, especialidad, precio_base):

        super().__init__("Asesoría", precio_base)

        self.tipo = "asesoria"
        self._nombre = especialidad
        self.especialidad = especialidad

    def calcular_costo(self, duracion):

        return self._precio_base * duracion

    def describir_servicio(self):

        return f"Asesoría en {self.especialidad}\nPrecio: {self.precio_base}"