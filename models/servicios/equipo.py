from models.servicio import Servicio #importamos los comportamiento heredados de la clase padre Servicio

# La clase ServicioEquipo representa un servicio de alquiler de equipo con un tipo específico.
class ServicioEquipo(Servicio):
    # El constructor de la clase ServicioEquipo recibe el tipo de equipo y el precio base del servicio.
    def __init__(self,tipo_equipo, precio_base):
        super().__init__(f"Equipo", precio_base) #llamamos al constructor de la clase padre
        #definimos el tipo de servicio como "equipo" y asignamos el tipo de equipo al atributo correspondiente.
        self.tipo = "equipo"
        self.tipo_equipo = tipo_equipo
        self._nombre = self.tipo_equipo

    #calculo del costo total del servicio, multiplicando el precio base por la duración del alquiler.
    def calcular_costo(self, duracion):
        return self._precio_base * duracion

    #metodo para describir el servicio, mostrando el tipo de equipo y el precio base
    def describir_servicio(self):
        return f"Alquiler de {self.tipo_equipo}\nPrecio: {self.precio_base}$"