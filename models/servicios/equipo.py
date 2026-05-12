from models.servicio import Servicio


class ServicioEquipo(Servicio):

    def __init__(self,tipo_equipo, precio_base):

        super().__init__(f"Equipo", precio_base)

        self.tipo = "equipo"
        self.tipo_equipo = tipo_equipo
        self._nombre = self.tipo_equipo

    def calcular_costo(self, duracion):

        return self._precio_base * duracion

    def describir_servicio(self):

        return f"Alquiler de {self.tipo_equipo}\nPrecio: {self.precio_base}"