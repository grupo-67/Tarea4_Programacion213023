#implementamos clase y metodos abstratos
from abc import ABC, abstractmethod

#clase abstracta
class Entidad(ABC):
    def __init__(self, id, fecha_creacion):
        self.id = id
        self.fecha_creacion = fecha_creacion

    #metodo abstacto de la clase
    @abstractmethod
    def mostrar_informacion():
        pass