# controllers/reserva_controller.py

from models.reserva import Reserva

from utils.json_utils import JsonUtils
from utils.logger import Logger


class ReservaController:

    def __init__(self, cliente_controller, servicio_controller):

        self.cliente_controller = cliente_controller
        self.servicio_controller = servicio_controller

        self.reservas = JsonUtils.cargar_reservas(
            self.cliente_controller.clientes,
            self.servicio_controller.servicios
        )

    # =====================================================
    # CREAR RESERVA
    # =====================================================

    def crear_reserva(self, email_cliente, indice_servicio, duracion):

        try:

            cliente = self.cliente_controller.buscar_cliente(email_cliente)

            if not cliente:
                raise Exception("Cliente no encontrado")

            servicio = self.servicio_controller.buscar_servicio(indice_servicio)

            if not servicio:
                raise Exception("Servicio no encontrado")

            reserva = Reserva(
                cliente,
                servicio,
                duracion
            )

            reserva.confirmar()

            self.reservas.append(reserva)

            JsonUtils.guardar_reservas(self.reservas)

            return True, "Reserva creada correctamente"

        except Exception as e:

            Logger.guardar_log(str(e))

            return False, str(e)

    # =====================================================
    # LISTAR RESERVAS
    # =====================================================

    def listar_reservas(self):

        return self.reservas

    # =====================================================
    # CANCELAR RESERVA
    # =====================================================

    def cancelar_reserva(self, indice):

        try:

            reserva = self.reservas[indice]

            reserva.cancelar()

            JsonUtils.guardar_reservas(self.reservas)

            return True, "Reserva cancelada"

        except Exception as e:

            Logger.guardar_log(str(e))

            return False, str(e)