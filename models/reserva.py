# clase reserva
# clases de Santiago
import logging


# Configuración del sistema de logs
logging.basicConfig(
    filename='sistema.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


# Excepción personalizada
class ReservaError(Exception):
    """
    Excepción personalizada para errores de reservas.
    """
    pass


class Reserva:
    """
    Clase encargada de gestionar las reservas
    del sistema.
    """

    def __init__(self, cliente, servicio, duracion):

        # Validación de duración
        if duracion <= 0:
            raise ReservaError(
                "La duración de la reserva debe ser mayor a cero"
            )

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        """
        Método para confirmar una reserva.
        """

        try:

            costo = self.servicio.calcular_costo()

            if costo <= 0:
                raise ReservaError(
                    "El costo de la reserva no es válido"
                )

        except ReservaError as error:

            logging.error(
                f"Error al confirmar reserva: {error}"
            )

            print(f"Error: {error}")

        else:

            self.estado = "Confirmada"

            print("Reserva confirmada correctamente")

        finally:

            print("Proceso de confirmación finalizado")

    def cancelar(self):
        """
        Método para cancelar una reserva.
        """

        try:

            if self.estado == "Cancelada":
                raise ReservaError(
                    "La reserva ya se encuentra cancelada"
                )

            self.estado = "Cancelada"

            print("Reserva cancelada correctamente")

        except ReservaError as error:

            logging.error(
                f"Error al cancelar reserva: {error}"
            )

            print(f"Error: {error}")

    def procesar(self):
        """
        Método para procesar la reserva.
        """

        try:

            if self.estado != "Confirmada":
                raise ReservaError(
                    "No se puede procesar una reserva no confirmada"
                )

            print("Procesando reserva...")

        except ReservaError as error:

            logging.error(
                f"Error al procesar reserva: {error}"
            )

            print(f"Error: {error}")

    def mostrar_informacion(self):
        """
        Muestra la información de la reserva.
        """

        print("========== RESERVA ==========")
        print(f"Cliente: {self.cliente}")
        print(f"Servicio: {self.servicio}")
        print(f"Duración: {self.duracion}")
        print(f"Estado: {self.estado}")
        print("================================")