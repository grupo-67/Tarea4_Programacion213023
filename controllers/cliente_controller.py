#importamos las clases necesarias para el funcionamiento del controlador cliente
from models.cliente import Cliente
from utils.json_utils import JsonUtils
from utils.logger import Logger
import re

class ClienteController:
    #Constructor de controller cliente
    def __init__(self):
        self.clientes = JsonUtils.cargar_clientes()

    # REGISTRAR CLIENTE
    def registrar_cliente(self, nombre, email, telefono):
        # Validar campos y registrar cliente, devolviendo tupla (exito, mensaje)
        try:
            nombre = nombre.strip()
            email = email.strip()
            telefono = telefono.strip()

            # VALIDACIONES
            if not nombre or not email or not telefono:
                raise Exception("Todos los campos son obligatorios")

            # Validar formato de Email
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                raise Exception("El formato de correo electrónico no es válido")
            
            # Validar formato de Teléfono (solo números, min 7 dígitos)
            if not telefono.isdigit() or len(telefono) < 7:
                raise Exception("El teléfono debe contener solo números y al menos 7 dígitos")
            
            # Validar duplicados por EMAIL
            if any(c.email == email for c in self.clientes):
                raise Exception("Ya existe un cliente registrado con este correo")
            
            # VALIDAR DUPLICADOS
            cliente_existente = self.buscar_cliente(email)

            if cliente_existente:
                raise Exception("El cliente ya existe")

            cliente = Cliente(nombre, email, telefono)
            self.clientes.append(cliente)   # Agregar el nuevo cliente a la lista de clientes
            JsonUtils.guardar_clientes(self.clientes) # Guardar la lista actualizada de clientes en el archivo JSON

            return True, "Cliente registrado correctamente"

        except Exception as e:
            Logger.guardar_log(str(e)) # Guardar el error en el log
            return False, str(e) # Devolver el mensaje de error para mostrarlo en la interfaz

    # BUSCAR CLIENTE Funcion no utilizada en la interfaz pero necesaria para validar duplicados y eliminar clientes.
    def buscar_cliente(self, nombre):
        for cliente in self.clientes:
            if cliente.nombre == nombre:
                return cliente
        return None

    # LISTAR CLIENTES
    def listar_clientes(self):
        return self.clientes

    # ELIMINAR CLIENTE Funcion no utilizada en la interfaz pero necesaria para eliminar clientes.
    def eliminar_cliente(self, email):
        try:
            cliente = self.buscar_cliente(email) # Buscar el cliente por email para eliminarlo

            if not cliente:
                raise Exception("Cliente no encontrado")

            self.clientes.remove(cliente)
            JsonUtils.guardar_clientes(self.clientes)

            return True, "Cliente eliminado correctamente"

        except Exception as e:
            Logger.guardar_log(str(e))
            return False, str(e)