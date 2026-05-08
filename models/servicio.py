# implementamos clase y métodos abstractos

from abc import ABC, abstractmethod


# clase abstracta servicio
class Servicio(ABC):

    def __init__(self, nombre_servicio, precio_base):

        # Validación del nombre
        if nombre_servicio == "":
            raise ValueError(
                "El nombre del servicio no puede estar vacío"
            )

        # Validación del precio
        if precio_base <= 0:
            raise ValueError(
                "El precio base debe ser mayor a cero"
            )

        self.nombre_servicio = nombre_servicio
        self.precio_base = precio_base
        self.disponible = True

    # método abstracto calcular costo
    @abstractmethod
    def calcular_costo(self):
        pass

    # método abstracto describir servicio
    @abstractmethod
    def describir_servicio(self):
        pass

    # método para cambiar disponibilidad
    def cambiar_disponibilidad(self, estado):

        if type(estado) != bool:
            raise ValueError(
                "El estado debe ser True o False"
            )

        self.disponible = estado

    # método para mostrar información general
    def mostrar_informacion(self):

        disponibilidad = (
            "Disponible"
            if self.disponible
            else "No disponible"
        )

        print("======= SERVICIO =======")
        print(f"Nombre: {self.nombre_servicio}")
        print(f"Precio Base: ${self.precio_base}")
        print(f"Estado: {disponibilidad}")
        print("========================")