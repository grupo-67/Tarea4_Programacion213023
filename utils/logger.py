# utils/logger.py
from datetime import datetime #importamos datetime para poder registrar la fecha y hora de cada log

# Clase Logger para manejar el registro de eventos importantes del sistema en un archivo de texto
class Logger:
    # Método estático para guardar un mensaje de log en el archivo "logs.txt"
    @staticmethod
    def guardar_log(mensaje): # metodo para guardar un mensaje de log, recibe el mensaje como parámetro
        with open("logs.txt", "a", encoding="utf-8") as f:
            f.write(
                f"[{datetime.now()}] {mensaje}\n"
            )