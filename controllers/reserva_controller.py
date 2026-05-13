# controllers/reserva_controller.py
#importacion del modelo reservas y utilidades necesarias.
from models.reserva import Reserva
from utils.json_utils import JsonUtils
from utils.logger import Logger

class ReservaController:
    #constructor del controlador de reservas, recibe los controladores de cliente y servicio para poder cargar las reservas desde el json.
    def __init__(self, cliente_controller, servicio_controller):
        self.cliente_controller = cliente_controller
        self.servicio_controller = servicio_controller
        self.reservas = JsonUtils.cargar_reservas(
            self.cliente_controller.clientes,
            self.servicio_controller.servicios
        )

    # CREAR RESERVA
    def crear_reserva(self, nombre_cliente, indice_servicio, duracion, fecha):
        try:
            # Validaciones de entrada
            if not nombre_cliente or indice_servicio is None or not fecha:
                raise Exception("Faltan datos obligatorios para la reserva")
            # Validar que la duración sea un número entero positivo
            try:
                duracion_int = int(duracion)
            except:
                raise Exception("La duración debe ser un número entero")

            cliente = self.cliente_controller.buscar_cliente(nombre_cliente)
            servicio = self.servicio_controller.buscar_servicio(indice_servicio)

            if not cliente or not servicio:
                raise Exception("Cliente o Servicio no encontrados")

            # La reserva nace "Pendiente"
            reserva = Reserva(cliente, servicio, duracion_int, fecha)
            
            self.reservas.append(reserva)
            JsonUtils.guardar_reservas(self.reservas)
            return True, "Reserva registrada (Pendiente de confirmación)"
        
        except Exception as e:
            Logger.guardar_log(str(e))
            return False, str(e)

    # CONFIRMAR RESERVA 
    def confirmar_reserva(self, indice):
        # Validar que el índice sea un número entero válido
        try:
            reserva = self.reservas[indice]
            reserva.confirmar() 
        
            # Guardar cambios para que no se borren al cerrar
            JsonUtils.guardar_reservas(self.reservas)
            return True, "Reserva confirmada correctamente"
        except Exception as e:
            Logger.guardar_log(str(e))
            return False, str(e)

    # LISTAR RESERVAS
    def listar_reservas(self):
        return self.reservas

    # CANCELAR RESERVA
    def cancelar_reserva(self, indice):
        try:
            reserva = self.reservas[indice]
            reserva.cancelar()
            JsonUtils.guardar_reservas(self.reservas)
            return True, "Reserva cancelada"
        
        except Exception as e:
            Logger.guardar_log(str(e))
            return False, str(e)
    
    # ACTUALIZAR RESERVA sin utilizar (pendiente de implementación en la vista, para proxima actualización)
    def actualizar_reserva(self, indice, nombre_cliente, indice_servicio, duracion, fecha):
        try:
            # Buscamos los nuevos objetos para no perder datos
            cliente = self.cliente_controller.buscar_cliente(nombre_cliente)
            servicio = self.servicio_controller.buscar_servicio(indice_servicio)
            
            reserva = self.reservas[indice]
            reserva.cliente = cliente
            reserva.servicio = servicio
            reserva.duracion = int(duracion)
            reserva.fecha = fecha
            
            JsonUtils.guardar_reservas(self.reservas)
            return True, "Editado con éxito"
        except Exception as e:
            Logger.guardar_log(str(e))
            return False, str(e)