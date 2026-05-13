# controllers/servicio_controller.py
#importacion de los modelos de servicios, utilidades necesarias y logger para manejo de errores.
from models.servicios.asesoria import ServicioAsesoria
from models.servicios.sala import ServicioSala
from models.servicios.equipo import ServicioEquipo
from utils.json_utils import JsonUtils
from utils.logger import Logger

#controlador encargado de gestionar los servicios del sistema, permite registrar nuevos servicios, listar los existentes y buscar por índice.
class ServicioController:
    #constructor del controlador de servicios, carga los servicios desde el json al iniciar el programa.
    def __init__(self):
        self.servicios = JsonUtils.cargar_servicios()

    # REGISTRAR SERVICIO
    def registrar_servicio(self, tipo, datos):
        # Validar que se hayan proporcionado los datos necesarios para el tipo de servicio
        try:
            servicio = None

            if tipo == "asesoria":
                servicio = ServicioAsesoria(
                    datos["especialidad"],
                    datos["precio"]
                )

            elif tipo == "sala":
                servicio = ServicioSala(
                    datos["nombre"],
                    datos["capacidad"],
                    datos["precio"]
                )

            elif tipo == "equipo":
                servicio = ServicioEquipo(
                    datos["nombre"],
                    datos["precio"]
                )
            else:
                raise Exception(
                    "Tipo de servicio inválido"
                )

            # Si llegamos aquí, el servicio se creó correctamente, lo agregamos a la lista y guardamos
            self.servicios.append(servicio)
            JsonUtils.guardar_servicios(
                self.servicios
            )

            return True, "Servicio registrado correctamente" # Mensaje de éxito

        # Si ocurre cualquier error, lo capturamos, guardamos en el log y devolvemos un mensaje de error
        except Exception as e:
            Logger.guardar_log(str(e))
            return False, str(e)

    # LISTAR SERVICIOS
    def listar_servicios(self):
        return self.servicios

    # BUSCAR SERVICIO
    def buscar_servicio(self, indice):
        # Validar que el índice sea un número entero válido
        try:
            return self.servicios[indice]
        except:
            return None