from models.servicio import Servicio


class ServicioSala(Servicio):

    def __init__(self, capacidad, horas, precio_base):

        super().__init__("Sala", precio_base)

        self.capacidad = capacidad
        self.horas = horas

    def calcular_costo(self):

        return self._precio_base * self.horas

    def describir_servicio(self):

        return f"Sala para {self.capacidad} personas"
