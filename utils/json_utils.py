# importacion de librerias y modelos necesarios para la gestion de archivos JSON
import json
import os
#importamos los modelos para convertirlos a diccionarios y viceversa
from models.cliente import Cliente
from models.reserva import Reserva
from models.servicios.asesoria import ServicioAsesoria
from models.servicios.sala import ServicioSala
from models.servicios.equipo import ServicioEquipo

# Clase de utilidades para manejar la persistencia de datos en formato JSON.
class JsonUtils:
    # Rutas de los archivos JSON para clientes, servicios y reservas.
    CLIENTES_PATH = "data/clientes.json"
    SERVICIOS_PATH = "data/servicios.json"
    RESERVAS_PATH = "data/reservas.json"

    # CREAR CARPETA Y ARCHIVOS
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

    # CLIENTES
    @staticmethod
    def guardar_clientes(clientes): #metodo para guardar clientes en formato JSON, recibe una lista de objetos Cliente
        datos = []

        for cliente in clientes:
            datos.append(cliente.to_dict())

        with open(JsonUtils.CLIENTES_PATH, "w") as f:
            json.dump(datos, f, indent=4)

    @staticmethod
    def cargar_clientes(): #metodo para cargar clientes desde un archivo JSON, devuelve una lista de objetos Cliente
        JsonUtils.inicializar_json()
        clientes = []

        with open(JsonUtils.CLIENTES_PATH, "r") as f:
            datos = json.load(f)
        # iteramos sobre cada item del JSON y creamos un objeto Cliente con los datos correspondientes
        for item in datos:
            cliente = Cliente(
                item["nombre"],
                item["email"],
                item["telefono"]
            )

            cliente.id = item.get("id")
            cliente.fecha_creacion = item.get("fecha_creacion") 
            clientes.append(cliente) #agregamos el cliente a la lista de clientes
        return clientes

    # SERVICIOS
    @staticmethod
    def guardar_servicios(servicios): #metodo para guardar servicios en formato JSON, recibe una lista de objetos Servicio
        datos = []
        # iteramos sobre cada servicio y creacmos un diccionario con los datos necesarios
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
            json.dump(datos, f, indent=4) # guardamos la lista

    @staticmethod
    def cargar_servicios(): #metodo para cargar servicios desde un archivo JSON, devuelve una lista de objetos Servicio
        JsonUtils.inicializar_json()
        servicios = []

        with open(JsonUtils.SERVICIOS_PATH, "r") as f:

            datos = json.load(f)

        # iteramos sobre cada item del Json y creamos un objeto Servicio correspondiente segun el tipo de servicio
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

            servicios.append(servicio) #agregamos el servicio a la lista de servicios
        return servicios

    # RESERVAS
    @staticmethod
    def guardar_reservas(reservas): #metodo para guardar reservas en formato JSON, recibe una lista de objetos Reserva
        datos = [reserva.to_dict() for reserva in reservas]
        with open(JsonUtils.RESERVAS_PATH, "w") as f:
            json.dump(datos, f, indent=4)

    @staticmethod
    def cargar_reservas(clientes, servicios): #metodo para cargar reservas desde un archivo JSON
        JsonUtils.inicializar_json()
        reservas = []
        # iteramos sobre cada item del JSON
        try:
            with open(JsonUtils.RESERVAS_PATH, "r") as f:
                datos = json.load(f)
            
            for item in datos:
                cliente = next((c for c in clientes if c.nombre == item["cliente_nombre"]), None)
                servicio = next((s for s in servicios if s.nombre == item["servicio_nombre"]), None)
                # si encontramos el cliente y el servicio correspondientes, creamos un objeto Reserva con los datos del JSON
                if cliente and servicio:
                    duracion = item.get("duracion", 1)
                    fecha = item.get("fecha", "No definida")
                    reserva = Reserva(cliente, servicio, duracion, fecha)
                    reserva.estado = item["estado"]
                    reserva.costo = item.get("costo", 0.0)
                    reservas.append(reserva)

        except Exception as e:
            print(f"Error cargando reservas: {e}")
        return reservas