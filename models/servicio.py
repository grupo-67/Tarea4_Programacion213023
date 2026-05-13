# implementamos clase y métodos abstractos
from abc import ABC, abstractmethod

#clase servicio para manejar los servicios que ofrece el negocio, con sus atributos y metodos.
class Servicio(ABC):
    #constructor de la clase servicio, recibe el nombre del servicio y su precio base.
    def __init__(self, nombre, precio_base):
        # Validaciones básicas para asegurar que los datos del servicio sean válidos.
        if not nombre.strip():
            raise ValueError("Nombre inválido")
        # Validamos que el precio base sea un número positivo
        if precio_base <= 0:
            raise ValueError("El precio debe ser mayor a 0")

        # Inicializamos los atributos del servicio
        self._nombre = nombre
        self._precio_base = precio_base
        self._disponible = True

    # Métodos abstractos que deben ser implementados por las clases hijas para calcular el costo del servicio y describirlo.
    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    # GETTERS
    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    @property
    def disponible(self):
        return self._disponible