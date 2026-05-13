#importamos necesarios para la interfaz
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from controllers.servicio_controller import ServicioController
from views.panels.nuevo_servicio_view import NuevoServicioView

# Panel para gestionar los servicios del sistema.
class ServiciosPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.controller = ServicioController()
        self.crear_ui()
        self.cargar_servicios()

    # Método para crear la interfaz gráfica del panel de servicios.
    def crear_ui(self):
        tk.Label(self, text="Servicios", font=("Segoe UI", 22, "bold"), 
                 bg="white", fg="#333").pack(anchor="w", padx=30, pady=(20, 10))

        # TABLA
        tabla_cont = tk.Frame(self, bg="white", highlightbackground="#EEE", highlightthickness=1)
        tabla_cont.pack(fill="both", expand=True, padx=30, pady=10)

        # Definimos las columnas de la tabla y configuramos sus encabezados
        columnas = ("id", "tipo", "nombre", "precio")
        self.tabla = ttk.Treeview(tabla_cont, columns=columnas, show="headings")
        
        # Configuramos cada columna para que se ajuste al contenido y tenga un encabezado descriptivo
        for col in columnas:
            self.tabla.heading(col, text=col.capitalize())
            self.tabla.column(col, anchor="center")
        self.tabla.pack(fill="both", expand=True)

        #BOTONES
        btns_frame = tk.Frame(self, bg="white")
        btns_frame.pack(fill="x", padx=30, pady=20)

        # Botón para ver los detalles del servicio seleccionado en la tabla
        tk.Button(btns_frame, text="Ver Detalles", relief="flat", 
                  highlightthickness=1, highlightbackground="#CCC",
                  padx=15, pady=5, command=self.ver_detalles).pack(side="left", padx=5)

        # Botón para abrir el formulario de creación de un nuevo servicio
        tk.Button(btns_frame, text="Agregar un nuevo servicio", relief="flat",
                  highlightthickness=1, highlightbackground="#CCC",
                  padx=15, pady=5, command=self.abrir_formulario_nuevo).pack(side="left", padx=5)

    # Método para abrir el formulario de creación de un nuevo servicio
    def abrir_formulario_nuevo(self):
        NuevoServicioView(self, self.controller)

    # Método para cargar los servicios desde el controlador y mostrarlos en la tabla
    def cargar_servicios(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        servicios = self.controller.listar_servicios()

        for i, servicio in enumerate(servicios, start=1):
            tipo = servicio.__class__.__name__.replace("Servicio", "")
            self.tabla.insert(
                "",
                "end",
                values=(
                    i,
                    tipo,
                    servicio.nombre,
                    servicio.precio_base
                )
            )

    # Método para mostrar los detalles del servicio seleccionado en la tabla
    def ver_detalles(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione un servicio de la tabla")
            return

        # Obtenemos el índice de la fila seleccionada
        indice = self.tabla.index(seleccion[0])
        servicio = self.controller.buscar_servicio(indice)

        if servicio:
            # Llamada al método mostrar_informacion() del modelo
            detalle = servicio.describir_servicio()
            messagebox.showinfo("Detalles del Servicio", detalle)