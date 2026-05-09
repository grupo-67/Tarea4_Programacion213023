# utils/logger.py

from datetime import datetime


class Logger:

    @staticmethod
    def guardar_log(mensaje):

        with open("logs.txt", "a", encoding="utf-8") as f:

            f.write(
                f"[{datetime.now()}] {mensaje}\n"
            )