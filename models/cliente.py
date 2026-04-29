class Cliente:
    def __init__(self, nombre, telefono, email):
        self._nombre = nombre
        self._telefono = telefono
        self._email = email

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def telefono(self):
        return self._telefono
    
    @property
    def email(self):
        return self._email