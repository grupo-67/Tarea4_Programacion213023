# importamos los comportamiento heredados de la clase padre Servicio
from models.servicio import Servicio
# Importamos la excepción para el manejo robusto de errores
from models.excepciones import DatosInvalidosError

class ServicioSala(Servicio):
    def __init__(self, tipo_sala, capacidad, horas, precio_hora):
        # super().__init__ envía el nombre general y el precio base a la clase padre
        super().__init__("Reserva de Sala", precio_hora) 
        self.tipo_sala = tipo_sala # Ejemplo: 'Juntas', 'Audiovisuales', 'Sistemas'
        self.capacidad = capacidad
        self.horas = horas

    # Implementamos el método obligatorio (Polimorfismo)
    def calcular_costo(self, descuento=0, es_festivo=False):
        """
        Calcula el costo por horas.
        Incluye validación estricta y sobrecarga (parámetro es_festivo).
        """
        if self.horas <= 0 or self.capacidad <= 0:
            raise DatosInvalidosError("Las horas y la capacidad deben ser valores positivos.")
        
        if descuento < 0:
            raise DatosInvalidosError("El descuento no puede ser negativo.")
        
        total = self.precio_base * self.horas
        
        # Si es festivo, aplicamos un recargo del 20%
        if es_festivo:
            total *= 1.20
        
        # Retornamos el total aplicando el descuento opcional
        return max(0, total - descuento)

    # Implementamos la descripción obligatoria
    def describir_servicio(self):
        return f"Sala de {self.tipo_sala} | Capacidad: {self.capacidad} personas | Tiempo: {self.horas}h"
