class Reserva:

    def __init__(self, cliente, servicio, duracion):

        if duracion <= 0:
            raise ValueError(
                "La duración debe ser mayor a cero"
            )

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion

        self.estado = "Pendiente"

    # ==========================================
    # CONFIRMAR RESERVA
    # ==========================================

    def confirmar(self):

        costo = self.servicio.calcular_costo()

        if costo <= 0:
            raise ValueError(
                "El costo del servicio no es válido"
            )

        self.estado = "Confirmada"

    # ==========================================
    # CANCELAR RESERVA
    # ==========================================

    def cancelar(self):

        if self.estado == "Cancelada":
            raise ValueError(
                "La reserva ya fue cancelada"
            )

        self.estado = "Cancelada"

    # ==========================================
    # PROCESAR RESERVA
    # ==========================================

    def procesar(self):

        if self.estado != "Confirmada":
            raise ValueError(
                "La reserva debe estar confirmada"
            )

        self.estado = "Procesada"

    # ==========================================
    # MOSTRAR INFORMACIÓN
    # ==========================================

    def mostrar_informacion(self):

        return (
            f"{self.cliente.nombre} | "
            f"{self.servicio.nombre} | "
            f"{self.estado}"
        )