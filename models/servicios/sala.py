from models.servicio import Servicio #importamos los comportamiento heredados de la clase padre Servicio

# La clase ServicioSala representa un servicio de reserva de sala con un tipo específico y una capacidad determinada.
class ServicioSala(Servicio):
    # El constructor de la clase ServicioSala recibe el tipo de sala, la capacidad y el precio base del servicio.
    def __init__(self, tipo_sala, capacidad, precio_base):
        super().__init__("Reserva de Sala", precio_base) #llamamos al constructor de la clase padre

        self.tipo = "sala"
        self._nombre = tipo_sala
        self.capacidad = capacidad

    #calculo del costo total del servicio, multiplicando el precio base por la duración de la reserva.
    def calcular_costo(self, duracion):
        return self._precio_base * duracion

    #metodo para describir el servicio, mostrando el tipo de sala, la capacidad y el precio base
    def describir_servicio(self):
        return f"{self.nombre}\nCapacidad: {self.capacidad} Personas\nPrecio: {self.precio_base}$"