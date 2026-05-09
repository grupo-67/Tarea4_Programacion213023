# utils/json_utils.py

import json
import os

from models.cliente import Cliente
from models.reserva import Reserva

from models.servicios.asesoria import ServicioAsesoria
from models.servicios.sala import ServicioSala
from models.servicios.equipo import ServicioEquipo


class JsonUtils:

    CLIENTES_PATH = "data/clientes.json"
    SERVICIOS_PATH = "data/servicios.json"
    RESERVAS_PATH = "data/reservas.json"

    # =====================================================
    # CREAR CARPETA Y ARCHIVOS
    # =====================================================

    @staticmethod
    def inicializar_json():

        os.makedirs("data", exist_ok=True)

        archivos = [
            JsonUtils.CLIENTES_PATH,
            JsonUtils.SERVICIOS_PATH,
            JsonUtils.RESERVAS_PATH
        ]

        for archivo in archivos:

            if not os.path.exists(archivo):

                with open(archivo, "w") as f:
                    json.dump([], f)

    # =====================================================
    # CLIENTES
    # =====================================================

    @staticmethod
    def guardar_clientes(clientes):

        datos = []

        for cliente in clientes:

            datos.append({
                "nombre": cliente._nombre,
                "email": cliente._email,
                "telefono": cliente._telefono
            })

        with open(JsonUtils.CLIENTES_PATH, "w") as f:

            json.dump(datos, f, indent=4)

    @staticmethod
    def cargar_clientes():

        JsonUtils.inicializar_json()

        clientes = []

        with open(JsonUtils.CLIENTES_PATH, "r") as f:

            datos = json.load(f)

        for item in datos:

            cliente = Cliente(
                item["nombre"],
                item["email"],
                item["telefono"]
            )

            clientes.append(cliente)

        return clientes

    # =====================================================
    # SERVICIOS
    # =====================================================

    @staticmethod
    def guardar_servicios(servicios):

        datos = []

        for servicio in servicios:

            if isinstance(servicio, ServicioAsesoria):

                datos.append({
                    "tipo": "asesoria",
                    "especialidad": servicio.especialidad,
                    "horas": servicio.horas,
                    "precio": servicio._precio_base
                })

            elif isinstance(servicio, ServicioSala):

                datos.append({
                    "tipo": "sala",
                    "capacidad": servicio.capacidad,
                    "horas": servicio.horas,
                    "precio": servicio._precio_base
                })

            elif isinstance(servicio, ServicioEquipo):

                datos.append({
                    "tipo": "equipo",
                    "tipo_equipo": servicio.tipo,
                    "dias": servicio.dias,
                    "precio": servicio._precio_base
                })

        with open(JsonUtils.SERVICIOS_PATH, "w") as f:

            json.dump(datos, f, indent=4)

    @staticmethod
    def cargar_servicios():

        JsonUtils.inicializar_json()

        servicios = []

        with open(JsonUtils.SERVICIOS_PATH, "r") as f:

            datos = json.load(f)

        for item in datos:

            if item["tipo"] == "asesoria":

                servicio = ServicioAsesoria(
                    item["especialidad"],
                    item["horas"],
                    item["precio"]
                )

            elif item["tipo"] == "sala":

                servicio = ServicioSala(
                    item["capacidad"],
                    item["horas"],
                    item["precio"]
                )

            elif item["tipo"] == "equipo":

                servicio = ServicioEquipo(
                    item["tipo_equipo"],
                    item["dias"],
                    item["precio"]
                )

            servicios.append(servicio)

        return servicios

    # =====================================================
    # RESERVAS
    # =====================================================

    @staticmethod
    def guardar_reservas(reservas):

        datos = []

        for reserva in reservas:

            datos.append({
                "cliente": reserva.cliente._email,
                "servicio": reserva.servicio._nombre,
                "duracion": reserva.duracion,
                "estado": reserva.estado
            })

        with open(JsonUtils.RESERVAS_PATH, "w") as f:

            json.dump(datos, f, indent=4)

    @staticmethod
    def cargar_reservas(clientes, servicios):

        JsonUtils.inicializar_json()

        reservas = []

        with open(JsonUtils.RESERVAS_PATH, "r") as f:

            datos = json.load(f)

        for item in datos:

            cliente = None
            servicio = None

            for c in clientes:

                if c._email == item["cliente"]:
                    cliente = c
                    break

            for s in servicios:

                if s._nombre == item["servicio"]:
                    servicio = s
                    break

            if cliente and servicio:

                reserva = Reserva(
                    cliente,
                    servicio,
                    item["duracion"]
                )

                reserva.estado = item["estado"]

                reservas.append(reserva)

        return reservas