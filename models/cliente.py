#importamos la clase abstrata de entidad
from models.entidad import Entidad
from datetime import datetime
import uuid

#clase cliente que hereda de entidad, con sus atributos y métodos específicos para manejar la información del cliente.
class Cliente(Entidad):
    #constructor de la clase cliente
    def __init__(self, nombre, email, telefono):
        id = str(uuid.uuid4())[:8] #generador unico de id para cada cliente
        fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #fecha de creación del cliente

        super().__init__(id, fecha_creacion) #llamamos al constructor de la clase padre para inicializar los atributos heredados

        #inicializamos los atributos específicos del cliente
        self._nombre = nombre
        self._email = email
        self._telefono = telefono

    # GETTERS
    @property
    def nombre(self):
        return self._nombre

    @property
    def email(self):
        return self._email

    @property
    def telefono(self):
        return self._telefono

    # MOSTRAR INFORMACIÓN
    def mostrar_informacion(self):
        return f"Cliente: {self._nombre}\nTeléfono: {self.telefono}\nEmail: {self._email}\nCreado: {self.fecha_creacion}"

    # CONVERTIR A DICCIONARIO para facilitar la serialización y almacenamiento de los datos del cliente.
    def to_dict(self):
        return {
            "id": self.id,
            "fecha_creacion": self.fecha_creacion,
            "nombre": self._nombre,
            "email": self._email,
            "telefono": self._telefono
        }