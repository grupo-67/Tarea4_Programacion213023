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

            datos.append(cliente.to_dict())

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

            cliente.id = item.get("id")
            cliente.fecha_creacion = item.get("fecha_creacion")

            clientes.append(cliente)

        return clientes

    # =====================================================
    # SERVICIOS
    # =====================================================

    @staticmethod
    def guardar_servicios(servicios):

        datos = []

        for servicio in servicios:

            if servicio.tipo == "asesoria":

                datos.append({
                    "tipo": "asesoria",
                    "especialidad": servicio._nombre,
                    "precio": servicio.precio_base
                })

            elif servicio.tipo == "sala":

                datos.append({
                    "tipo": "sala",
                    "nombre": servicio._nombre,
                    "capacidad": servicio.capacidad,
                    "precio": servicio.precio_base
                })

            elif servicio.tipo == "equipo":

                datos.append({
                    "tipo": "equipo",
                    "nombre": servicio._nombre,
                    "precio": servicio.precio_base
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
                    item["precio"]
                )

            elif item["tipo"] == "sala":

                servicio = ServicioSala(
                    item["nombre"],
                    item["capacidad"],
                    item["precio"]
                )

            elif item["tipo"] == "equipo":

                servicio = ServicioEquipo(
                    item["nombre"],
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
                "cliente": reserva.cliente._nombre,
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