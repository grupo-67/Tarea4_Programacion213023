from models.servicio import Servicio


class ServicioSala(Servicio):

    def __init__(self, tipo_sala, capacidad, precio_base):

        super().__init__("Reserva de Sala", precio_base)

        self.tipo = "sala"
        self._nombre = tipo_sala
        self.capacidad = capacidad

    def calcular_costo(self, duracion):

        return self._precio_base * duracion

    def describir_servicio(self):

        return f"{self.nombre}\nCapacidad: {self.capacidad}\nPrecio: {self.precio_base}"
