#importamos la clase abstrata de entidad
from models.entidad import Entidad

#clase cliente 
class Cliente:
    def __init__(self, nombre, telefono, email):
        super().__init__()
        self._nombre = nombre
        self._telefono = telefono
        self._email = email

    #getter y setter para obtener datos del cliente
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def telefono(self):
        return self._telefono
    
    @property
    def email(self):
        return self._email
    
    #funcion para mostrar la informacion del cliente
    def mostrar_informacion(self):
        return f"{self._nombre} - {self.email}"