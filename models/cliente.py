#importamos la clase abstrata de entidad
from models.entidad import Entidad
from datetime import datetime
import uuid


class Cliente(Entidad):

    def __init__(self, nombre, email, telefono):

        id = str(uuid.uuid4())[:8]

        fecha_creacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        super().__init__(id, fecha_creacion)

        self._nombre = nombre
        self._email = email
        self._telefono = telefono

    # ==========================================
    # GETTERS
    # ==========================================

    @property
    def nombre(self):
        return self._nombre

    @property
    def email(self):
        return self._email

    @property
    def telefono(self):
        return self._telefono

    # ==========================================
    # MOSTRAR INFORMACIÓN
    # ==========================================

    def mostrar_informacion(self):

        return f"{self._nombre} - {self._email}"

    # ==========================================
    # CONVERTIR A DICCIONARIO
    # ==========================================

    def to_dict(self):

        return {
            "id": self.id,
            "fecha_creacion": self.fecha_creacion,
            "nombre": self._nombre,
            "email": self._email,
            "telefono": self._telefono
        }