#implementamos clase y metodos abstratos
from abc import ABC, abstractmethod

#clase abstrata servicio
class Servicio(ABC):
    def __init__(self, nombre_servicio, precio_base):
        self.nombre_servicio = nombre_servicio
        self.precio_base = precio_base
        self.disponible = True

    #metodo abstrato calcula costo
    @abstractmethod
    def calcular_costo(self):
        pass

    #metodos abstracto describir servicio
    @abstractmethod
    def describir_servicio(self):
        pass