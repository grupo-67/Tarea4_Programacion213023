from models.cliente import Cliente
from utils.json_utils import JsonUtils
from utils.logger import Logger


class ClienteController:

    def __init__(self):

        self.clientes = JsonUtils.cargar_clientes()

    # =====================================================
    # REGISTRAR CLIENTE
    # =====================================================

    def registrar_cliente(self, nombre, email, telefono):

        try:

            nombre = nombre.strip()
            email = email.strip()
            telefono = telefono.strip()

            # VALIDACIONES
            if not nombre or not email or not telefono:
                raise Exception("Todos los campos son obligatorios")

            # VALIDAR DUPLICADOS
            cliente_existente = self.buscar_cliente(email)

            if cliente_existente:
                raise Exception("El cliente ya existe")

            cliente = Cliente(nombre, email, telefono)

            self.clientes.append(cliente)

            JsonUtils.guardar_clientes(self.clientes)

            return True, "Cliente registrado correctamente"

        except Exception as e:

            Logger.guardar_log(str(e))

            return False, str(e)

    # =====================================================
    # BUSCAR CLIENTE
    # =====================================================

    def buscar_cliente(self, email):

        for cliente in self.clientes:

            if cliente.email == email:
                return cliente

        return None

    # =====================================================
    # LISTAR CLIENTES
    # =====================================================

    def listar_clientes(self):

        return self.clientes

    # =====================================================
    # ELIMINAR CLIENTE
    # =====================================================

    def eliminar_cliente(self, email):

        try:

            cliente = self.buscar_cliente(email)

            if not cliente:
                raise Exception("Cliente no encontrado")

            self.clientes.remove(cliente)

            JsonUtils.guardar_clientes(self.clientes)

            return True, "Cliente eliminado correctamente"

        except Exception as e:

            Logger.guardar_log(str(e))

            return False, str(e)