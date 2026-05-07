# importamos los comportamiento heredados de la clase padre Servicio
from models.servicio import Servicio
# Importamos la excepción personalizada
from models.excepciones import DatosInvalidosError

class ServicioEquipo(Servicio):
    def __init__(self, equipo_solicitado, cantidad_dias, precio_por_dia):
        """
        Constructor que envía los datos a la clase padre 'Servicio'.
        equipo_solicitado: Nombre del equipo (ej. 'Laptop HP')
        cantidad_dias: Días de alquiler
        precio_por_dia: Precio base por cada día
        """
        # Enviamos nombre y precio a self.nombre_servicio y self.precio_base de la clase padre
        super().__init__(f"Alquiler de {equipo_solicitado}", precio_por_dia)
        self.equipo_solicitado = equipo_solicitado
        self.cantidad_dias = cantidad_dias

    # Implementamos el método abstracto obligatorio de Servicio
    def calcular_costo(self, descuento=0, incluye_mantenimiento=False):
        """
        Calcula el costo total.
        Aplica polimorfismo y manejo de excepciones.
        """
        # Validación estricta según la guía
        if self.cantidad_dias <= 0 or self.precio_base <= 0:
            raise DatosInvalidosError("Los días y el precio base deben ser valores positivos.")

        # Lógica de cálculo: precio base (por día) * cantidad de días
        total = self.precio_base * self.cantidad_dias

        # Sobrecarga: Si se incluye mantenimiento preventivo, sumamos un 15%
        if incluye_mantenimiento:
            total *= 1.15

        # Aplicación de descuento opcional
        if descuento > 0:
            total -= (total * (descuento / 100))

        return round(total, 2)

    # Implementamos el segundo método abstracto de Servicio
    def describir_servicio(self):
        """
        Retorna la descripción específica del equipo y su estado.
        """
        estado = "Disponible" if self.disponible else "En uso/No disponible"
        return f"Servicio: {self.nombre_servicio} | Días: {self.cantidad_dias} | Estado: {estado}"