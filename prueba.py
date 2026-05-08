# =========================
# IMPORTACIONES
# =========================

from models.cliente import Cliente
from models.usser import Usuario

from models.servicios.asesoria import ServicioAsesoria
from models.servicios.equipo import ServicioEquipo
from models.servicios.sala import ServicioSala


# =========================
# FUNCIÓN PRINCIPAL
# =========================

def main():

    # =========================
    # PRUEBA USUARIO
    # =========================

    print("\n===== PRUEBA USUARIO =====")

    usuario = Usuario()

    if usuario.validar_usuario("programacion", "programacion"):
        print("✅ Usuario válido")
    else:
        print("❌ Usuario incorrecto")


    # =========================
    # PRUEBA CLIENTE
    # =========================

    print("\n===== PRUEBA CLIENTE =====")

    cliente1 = Cliente(
        "Carlos Mario",
        "3001234567",
        "carlos@gmail.com"
    )

    print(cliente1.mostrar_informacion())


    # =========================
    # PRUEBA SERVICIO ASESORIA
    # =========================

    print("\n===== PRUEBA ASESORIA =====")

    asesoria = ServicioAsesoria(
        "Python",
        5,
        50000
    )

    print(asesoria.describir_servicio())
    print("Costo total:", asesoria.calcular_costo())


    # =========================
    # PRUEBA SERVICIO EQUIPO
    # =========================

    print("\n===== PRUEBA EQUIPO =====")

    equipo = ServicioEquipo(
        "Laptop HP",
        3,
        80000
    )

    print(equipo.describir_servicio())

    print(
        "Costo total:",
        equipo.calcular_costo(
            descuento=10,
            incluye_mantenimiento=True
        )
    )


    # =========================
    # PRUEBA SERVICIO SALA
    # =========================

    print("\n===== PRUEBA SALA =====")

    sala = ServicioSala(
        "Audiovisuales",
        20,
        4,
        100000
    )

    print(
        "Costo sala:",
        sala.calcular_costo(
            descuento=50000,
            es_festivo=True
        )
    )

    print("\n✅ TODAS LAS PRUEBAS FINALIZADAS")


# =========================
# EJECUCIÓN PRINCIPAL
# =========================

if __name__ == "__main__":
    main()