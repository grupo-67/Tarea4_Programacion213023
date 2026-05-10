# implementamos clase y métodos abstractos

from abc import ABC, abstractmethod


class Servicio(ABC):

    def __init__(self, nombre, precio_base):

        if not nombre.strip():
            raise ValueError("Nombre inválido")

        if precio_base <= 0:
            raise ValueError("El precio debe ser mayor a 0")

        self._nombre = nombre
        self._precio_base = precio_base
        self._disponible = True

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    @property
    def disponible(self):
        return self._disponible