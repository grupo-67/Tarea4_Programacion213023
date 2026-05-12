# controllers/servicio_controller.py

from models.servicios.asesoria import ServicioAsesoria
from models.servicios.sala import ServicioSala
from models.servicios.equipo import ServicioEquipo

from utils.json_utils import JsonUtils
from utils.logger import Logger


class ServicioController:

    def __init__(self):

        self.servicios = JsonUtils.cargar_servicios()

    # =====================================================
    # REGISTRAR SERVICIO
    # =====================================================

    def registrar_servicio(self, tipo, datos):

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

            self.servicios.append(servicio)

            JsonUtils.guardar_servicios(
                self.servicios
            )

            return True, "Servicio registrado correctamente"

        except Exception as e:

            Logger.guardar_log(str(e))

            return False, str(e)

    # =====================================================
    # LISTAR SERVICIOS
    # =====================================================

    def listar_servicios(self):

        return self.servicios

    # =====================================================
    # BUSCAR SERVICIO
    # =====================================================

    def buscar_servicio(self, indice):

        try:

            return self.servicios[indice]

        except:

            return None