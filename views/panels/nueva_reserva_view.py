import tkinter as tk
from tkinter import ttk
import ctypes

class NuevaReservaView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Crear una nueva reserva")
        self.geometry("500x450")
        self.configure(bg="white")
        # Centrar ventana usando tu helper
        from utils.helpers import centrar_ventana
        centrar_ventana(self, 500, 450)
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()
        self.crear_ui()

    def crear_ui(self):
        container = tk.Frame(self, bg="white", padx=30, pady=20)
        container.pack(fill="both", expand=True)

        tk.Label(container, text="Crear una nueva reserva", font=("Segoe UI", 16, "bold"), 
                 bg="white", fg="#333").grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 20))

        # Configuración de columnas para que sean simétricas
        container.columnconfigure(0, weight=1)
        container.columnconfigure(1, weight=1)

        # Fila 1: Cliente y Servicio
        tk.Label(container, text="Cliente:", bg="white").grid(row=1, column=0, sticky="w")
        ttk.Combobox(container, state="readonly").grid(row=2, column=0, sticky="ew", padx=(0, 10), pady=(5, 15))

        tk.Label(container, text="Servicio:", bg="white").grid(row=1, column=1, sticky="w")
        ttk.Combobox(container, state="readonly").grid(row=2, column=1, sticky="ew", pady=(5, 15))

        # Fila 2: Fecha y Hora de inicio
        tk.Label(container, text="Fecha:", bg="white").grid(row=3, column=0, sticky="w")
        tk.Entry(container, highlightthickness=1, highlightbackground="#CCC", relief="flat").grid(row=4, column=0, sticky="ew", padx=(0, 10), pady=(5, 15), ipady=3)

        tk.Label(container, text="Hora de inicio:", bg="white").grid(row=3, column=1, sticky="w")
        tk.Entry(container, highlightthickness=1, highlightbackground="#CCC", relief="flat").grid(row=4, column=1, sticky="ew", pady=(5, 15), ipady=3)

        # Fila 3: Duración
        tk.Label(container, text="Duracion:", bg="white").grid(row=5, column=0, sticky="w")
        duracion_frame = tk.Frame(container, bg="white")
        duracion_frame.grid(row=6, column=0, sticky="w", pady=(5, 15))
        
        tk.Entry(duracion_frame, width=10, highlightthickness=1, highlightbackground="#CCC", relief="flat").pack(side="left", ipady=3)
        ttk.Combobox(duracion_frame, values=["Horas", "Días"], width=8, state="readonly").pack(side="left", padx=5)

        # Fila 4: Botones Finales
        btn_cancelar = tk.Button(container, text="Cancelar", bg="white", relief="flat", 
                                 highlightthickness=1, highlightbackground="#CCC", width=15,
                                 command=self.destroy)
        btn_cancelar.grid(row=7, column=0, sticky="w", pady=20)

        btn_confirmar = tk.Button(container, text="Confirmar reserva", bg="#4CB5FF", fg="white",
                                  relief="flat", font=("Segoe UI", 10, "bold"), padx=20)
        btn_confirmar.grid(row=7, column=1, sticky="e", pady=20)