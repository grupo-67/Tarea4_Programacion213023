import tkinter as tk
from tkinter import ttk
from views.panels.nueva_reserva_view import NuevaReservaView

class ReservasPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.crear_ui()

    def crear_ui(self):
        # Título
        tk.Label(self, text="Reservas", font=("Segoe UI", 22, "bold"), 
                 bg="white", fg="#333").pack(anchor="w", padx=30, pady=(20, 10))

        # --- CONTENEDOR PRINCIPAL (2 Columnas) ---
        main_container = tk.Frame(self, bg="white")
        main_container.pack(fill="both", expand=True, padx=30)

        # COLUMNA IZQUIERDA: Tabla
        left_frame = tk.Frame(main_container, bg="white")
        left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

        columnas = ("id", "cliente", "servicio", "fecha", "estado")
        self.tabla = ttk.Treeview(left_frame, columns=columnas, show="headings")
        for col in columnas:
            self.tabla.heading(col, text=col.capitalize())
            self.tabla.column(col, width=100, anchor="center")
        self.tabla.pack(fill="both", expand=True)

        # COLUMNA DERECHA: Detalles (Como en image_747811.png)
        right_frame = tk.LabelFrame(main_container, text="Detalles de la reserva", 
                                    font=("Segoe UI", 11, "bold"), bg="white",
                                    padx=15, pady=15, fg="#333", relief="flat",
                                    highlightbackground="#DDD", highlightthickness=1)
        # CORRECTO
        right_frame.pack(side="right", fill="both", expand=False, padx=(10, 0))
        # Si quieres que tenga un ancho fijo, asegúrate de que el LabelFrame 
        # tenga definido el width al crearse, aunque usualmente con el contenido basta.

        # Área de texto o info de detalles (puedes usar Labels dinámicos)
        self.txt_detalles = tk.Label(right_frame, text="Seleccione una reserva para ver detalles...", 
                                     bg="white", font=("Segoe UI", 10), justify="left", anchor="nw")
        self.txt_detalles.pack(fill="both", expand=True)

        # Botones de Acción (Confirmar, Cancelar, Editar)
        btns_detalles = tk.Frame(right_frame, bg="white")
        btns_detalles.pack(fill="x", pady=(10, 0))

        tk.Button(btns_detalles, text="Confirmar", bg="#5CFF5C", relief="flat", padx=10).pack(side="left", padx=2)
        tk.Button(btns_detalles, text="Cancelar", bg="#FF4C4C", fg="white", relief="flat", padx=10).pack(side="left", padx=2)
        tk.Button(btns_detalles, text="Editar", bg="#4CB5FF", fg="white", relief="flat", padx=10).pack(side="left", padx=2)

        # --- BOTÓN INFERIOR ---
        btn_nueva = tk.Button(self, text="Agregar nueva reserva", bg="white", relief="flat",
                              highlightthickness=1, highlightbackground="#CCC",
                              font=("Segoe UI", 10), padx=15, pady=5,
                              command=self.abrir_nueva_reserva)
        btn_nueva.pack(anchor="w", padx=30, pady=20)

    def abrir_nueva_reserva(self):
        NuevaReservaView(self)