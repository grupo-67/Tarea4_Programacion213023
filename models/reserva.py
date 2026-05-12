class Reserva:

    def __init__(self, cliente, servicio, duracion, fecha="No definida"):
        if duracion <= 0:
            raise ValueError(
                "La duración debe ser mayor a cero"
            )

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.fecha = fecha
        self.estado = "Pendiente"
        self.costo = 0.0

    # CONFIRMAR RESERVA
    def confirmar(self):
        # Asumiendo que el servicio tiene calcular_costo(duracion)
        self.costo = self.servicio.calcular_costo(self.duracion)
        if self.costo <= 0:
            raise ValueError("El costo calculado no es válido")
        self.estado = "Confirmada"

    # CANCELAR RESERVA
    def cancelar(self):

        if self.estado == "Cancelada":
            raise ValueError(
                "La reserva ya fue cancelada"
            )

        self.estado = "Cancelada"

    # PROCESAR RESERVA
    def procesar(self):

        if self.estado != "Confirmada":
            raise ValueError(
                "La reserva debe estar confirmada"
            )

        self.estado = "Procesada"

    # MOSTRAR INFORMACIÓN
    def mostrar_informacion(self):
        return (
            f"---Detalles de reserva---\n"
            f"Cliente: {self.cliente.nombre}\n"
            f"Servicio: {self.servicio.nombre}\n"
            f"Fecha: {self.fecha}\n"
            f"Duracion:{self.duracion}\n"
            f"Costo final: {self.costo:.2}\n"
             f"Estado: {self.estado}"
        )