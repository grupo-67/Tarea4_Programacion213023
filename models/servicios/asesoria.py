#importamos los comportamiento heredados de la clase padre Servicio
from models.servicio import Servicio


class ServicioAsesoria(Servicio):

    def __init__(self, especialidad, horas, precio_base):

        super().__init__("Asesoría", precio_base)

        self.especialidad = especialidad
        self.horas = horas

    def calcular_costo(self):

        return self._precio_base * self.horas

    def describir_servicio(self):

        return f"Asesoría en {self.especialidad}"