#importamos los comportamiento heredados de la clase padre Servicio
from models.servicio import Servicio

#clase servicio tipo asesoria
class ServicioAsesoria(Servicio):
    def __init__(self, especialidad, horas, precio_base):
        super().__init__("Asesoria", precio_base) 
        self.especialidad = especialidad
        self.horas = horas

    #funcion para calcular el costo total del servicio
    def calcular_costo(self):
        return self.precio_base * self.horas
    
    #funcion para descripbir el tipo de servicio
    def describir_servicio(self):
        return f"Asesoria en {self.especialidad}"