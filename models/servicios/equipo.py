from models.servicio import Servicio


class ServicioEquipo(Servicio):

    def __init__(self, tipo_equipo, dias, precio_base):

        super().__init__("Equipo", precio_base)

        self.tipo_equipo = tipo_equipo
        self.dias = dias

    def calcular_costo(self):

        return self._precio_base * self.dias

    def describir_servicio(self):

        return f"Alquiler de {self.tipo_equipo}"