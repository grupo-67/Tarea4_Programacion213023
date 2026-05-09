import tkinter as tk
from tkinter import ttk
from views.panels.nuevo_servicio_view import NuevoServicioView

class ServiciosPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.crear_ui()

    def crear_ui(self):
        tk.Label(self, text="Servicios", font=("Segoe UI", 22, "bold"), 
                 bg="white", fg="#333").pack(anchor="w", padx=30, pady=(20, 10))

        # --- TABLA ---
        tabla_cont = tk.Frame(self, bg="white", highlightbackground="#EEE", highlightthickness=1)
        tabla_cont.pack(fill="both", expand=True, padx=30, pady=10)

        columnas = ("id", "tipo", "nombre", "precio")
        self.tabla = ttk.Treeview(tabla_cont, columns=columnas, show="headings")
        
        for col in columnas:
            self.tabla.heading(col, text=col.capitalize())
            self.tabla.column(col, anchor="center")

        self.tabla.pack(fill="both", expand=True)

        # --- BOTONES ---
        btns_frame = tk.Frame(self, bg="white")
        btns_frame.pack(fill="x", padx=30, pady=20)

        tk.Button(btns_frame, text="Ver Detalles", relief="flat", 
                  highlightthickness=1, highlightbackground="#CCC",
                  padx=15, pady=5).pack(side="left", padx=5)

        tk.Button(btns_frame, text="Agregar un nuevo servicio", relief="flat",
                  highlightthickness=1, highlightbackground="#CCC",
                  padx=15, pady=5, command=self.abrir_formulario_nuevo).pack(side="left", padx=5)

    def abrir_formulario_nuevo(self):
        # Lanzamos la ventana secundaria
        NuevoServicioView(self)