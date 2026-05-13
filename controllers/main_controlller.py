# controllers/main_controller.py
#importando los controladores de cada entidad del sistema.
from controllers.cliente_controller import ClienteController
from controllers.servicio_controller import ServicioController
from controllers.reserva_controller import ReservaController
from utils.json_utils import JsonUtils

#controlador principal del sistema, encargado de gestionar controladores de cada entidad y utilidades necesarias.
class MainController:
    #constructor del controlador principal.
    def __init__(self):
        self.json_utils = JsonUtils
        self.cliente_controller = ClienteController()
        self.servicio_controller = ServicioController()
        self.reserva_controller = ReservaController(
            self.cliente_controller,
            self.servicio_controller
        )