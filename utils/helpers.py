#funcion para centrar la ventanas del inicion de session y sistema principal.
def centrar_ventana(ventana, ancho, alto):
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()

    x = int((pantalla_ancho / 2) - (ancho / 2))
    y = int((pantalla_alto / 2) - (alto / 2))

    ventana.geometry(f"{ancho}x{alto}+{x}+{y}")