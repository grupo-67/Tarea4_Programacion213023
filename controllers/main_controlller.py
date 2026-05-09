# controllers/main_controller.py

from controllers.cliente_controller import ClienteController
from controllers.servicio_controller import ServicioController
from controllers.reserva_controller import ReservaController


class MainController:

    def __init__(self):

        self.cliente_controller = ClienteController()

        self.servicio_controller = ServicioController()

        self.reserva_controller = ReservaController(
            self.cliente_controller,
            self.servicio_controller
        )