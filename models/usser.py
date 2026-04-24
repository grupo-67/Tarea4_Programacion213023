#clase usser como constructor con atributos y metodos para validar que los datos ingresados sean correctos
class Usuario:
    #atributos privados de la clase usser
    def __init__(self, nombre = None, contraseña = None):
        self._username = nombre
        self._password = contraseña

    #metodo para validar el usuario y contraseña digitados
    def validar_usuario(self, nombre, contraseña):
        return nombre == "programacion" and contraseña == "programacion"