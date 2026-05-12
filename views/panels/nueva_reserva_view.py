import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
import ctypes

class NuevaReservaView(tk.Toplevel):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.parent_panel = parent
        self.controller = controller
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass
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
        self.cargar_datos()

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
        self.combo_cliente = ttk.Combobox(
            container,
            state="readonly"
            )
        self.combo_cliente.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=(0, 10),
            pady=(5, 15)
        )

        #servicio
        # Tipo de servicio
        tk.Label(container, text="Tipo de Servicio:", bg="white").grid(
            row=1,
            column=1,
            sticky="w"
        )

        self.combo_tipo = ttk.Combobox(
            container,
            values=["Sala", "Equipo", "Asesoria"],
            state="readonly"
        )

        self.combo_tipo.grid(
            row=2,
            column=1,
            sticky="ew",
            pady=(5, 15)
        )

        self.combo_tipo.bind(
            "<<ComboboxSelected>>",
            self.actualizar_servicios
        )

        # Servicio específico
        tk.Label(container, text="Servicio:", bg="white").grid(
            row=3,
        column=0,
        sticky="w"
        )

        self.combo_servicio = ttk.Combobox(
            container,
            state="readonly"
        )

        self.combo_servicio.grid(
            row=4,
            column=0,
            sticky="ew",
            padx=(0, 10),
            pady=(5, 15)
        )

        # Fila 2: Fecha y Hora de inicio
        tk.Label(container, text="Fecha:", bg="white").grid(row=5, column=0, sticky="w")
        self.date_fecha = DateEntry(
            container,
            date_pattern="yyyy-mm-dd",
            background="#4C6EC0",
            foreground="white",
            borderwidth=1
        )

        self.date_fecha.grid(
            row=6,
            column=0,
            sticky="ew",
            padx=(0, 10),
        pady=(5, 15)
        )

        tk.Label(container, text="Hora de inicio:", bg="white").grid(row=5, column=1, sticky="w")
        self.combo_hora = ttk.Combobox(
            container,
            values=[
                f"{h:02}:00"
                for h in range(7, 23)
            ],
            state="readonly"
        )

        self.combo_hora.grid(
            row=6,
            column=1,
            sticky="ew",
        pady=(5, 15)
        )

        # Fila 3: Duración
        tk.Label(container, text="Duracion:", bg="white").grid(row=7, column=0, sticky="w")
        duracion_frame = tk.Frame(container, bg="white")
        duracion_frame.grid(row=8, column=0, sticky="w", pady=(5, 15))
        
        self.entry_duracion = tk.Entry(
            duracion_frame,
            width=10,
            highlightthickness=1,
            highlightbackground="#CCC",
            relief="flat"
        )
        self.entry_duracion.pack(
            side="left",
            ipady=3
        )
        ttk.Combobox(duracion_frame, values=["Horas", "Días"], width=8, state="readonly").pack(side="left", padx=5)

        # Fila 4: Botones Finales
        btn_cancelar = tk.Button(container, text="Cancelar", bg="white", relief="flat", 
                                 highlightthickness=1, highlightbackground="#CCC", width=15,
                                 command=self.destroy)
        btn_cancelar.grid(row=9, column=0, sticky="w", pady=20)

        btn_confirmar = tk.Button(
            container,
            text="Confirmar reserva",
            bg="#4CB5FF",
            fg="white",
            relief="flat",
            font=("Segoe UI", 10, "bold"),
            padx=20,
            command=self.guardar_reserva
        )
        btn_confirmar.grid(row=9, column=1, sticky="e", pady=20)

    def cargar_datos(self):

        clientes = self.controller.cliente_controller.listar_clientes()
        servicios = self.controller.servicio_controller.listar_servicios()

        self.clientes = clientes
        self.servicios = servicios

        self.combo_cliente["values"] = [
            cliente.nombre
            for cliente in clientes
        ]

        self.combo_servicio["values"] = [
            f"{i} - {servicio.nombre}"
            for i, servicio in enumerate(servicios)
        ]
    """
    def guardar_reserva(self):

        try:
            nombre_cliente = self.combo_cliente.get()
            servicio_texto = self.combo_servicio.get()

            if not servicio_texto:
                raise Exception(
                    "Seleccione un servicio"
                )

            indice_servicio = int(
                servicio_texto.split(" - ")[0]
            )

            duracion = int(
                self.entry_duracion.get()
            )

            exito, mensaje = self.controller.crear_reserva(
                nombre_cliente,
                indice_servicio,
                duracion
            )

            if exito:
                messagebox.showinfo(
                    "Éxito",
                    mensaje
                )

                self.parent_panel.cargar_reservas()
                self.destroy()

            else:
                messagebox.showerror(
                    "Error",
                    mensaje
                )

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )
    """
    def guardar_reserva(self):
        try:
            cliente = self.combo_cliente.get()
            servicio_raw = self.combo_servicio.get()
            fecha = self.date_fecha.get()
            duracion = self.entry_duracion.get()

            if not cliente or not servicio_raw or not duracion:
                raise Exception("Por favor rellene todos los campos")

            indice_ser = int(servicio_raw.split(" - ")[0])
            
            # Llamada al controlador
            exito, mensaje = self.controller.crear_reserva(cliente, indice_ser, duracion, fecha)

            if exito:
                messagebox.showinfo("Éxito", mensaje)
                self.parent_panel.cargar_reservas()
                self.destroy()
            else:
                messagebox.showerror("Error", mensaje)

        except Exception as e:
            messagebox.showerror("Validación", str(e))
            
    def actualizar_servicios(self, event=None):

        tipo = self.combo_tipo.get().lower()

        servicios = self.controller.servicio_controller.listar_servicios()

        filtrados = []

        for i, servicio in enumerate(servicios):

            if servicio.tipo.lower() == tipo:

                filtrados.append(
                    f"{i} - {servicio.nombre}"
                )

        self.combo_servicio["values"] = filtrados

        if filtrados:
            self.combo_servicio.current(0)