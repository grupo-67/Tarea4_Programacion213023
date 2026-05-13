#importaciones necesarias
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from views.panels.nueva_reserva_view import NuevaReservaView
from controllers.reserva_controller import ReservaController

# Panel de gestión de reservas, con tabla y detalles.
class ReservasPanel(tk.Frame):
    def __init__(self, parent,reserva_controller):
        super().__init__(parent, bg="white")
        self.controller = reserva_controller
        self.crear_ui()
        self.cargar_reservas()

    # Método para crear la interfaz de usuario del panel de reservas.
    def crear_ui(self):
        # Título
        tk.Label(self, text="Reservas", font=("Segoe UI", 22, "bold"), 
                 bg="white", fg="#333").pack(anchor="w", padx=30, pady=(20, 10))

        # CONTENEDOR PRINCIPAL
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

        # COLUMNA DERECHA: Detalles
        right_frame = tk.LabelFrame(main_container, text="Detalles de la reserva", 
                                    font=("Segoe UI", 11, "bold"), bg="white",
                                    padx=15, pady=15, fg="#333", relief="flat",
                                    highlightbackground="#DDD", highlightthickness=1)
        
        self.tabla.tag_configure("Pendiente", foreground="#E67E22") # Naranja suave
        self.tabla.tag_configure("Confirmada", foreground="#27AE60") # Verde esmeralda
        self.tabla.tag_configure("Cancelada", foreground="#C0392B")  # Rojo suave

        right_frame.pack(side="right", fill="both", expand=False, padx=(10, 0))
       
        # Etiqueta para mostrar detalles de la reserva seleccionada
        self.txt_detalles = tk.Label(right_frame, text="Seleccione una reserva para ver detalles...", 
                                     bg="white", font=("Segoe UI", 10), justify="left", anchor="nw", wraplength=250)
        self.txt_detalles.pack(fill="both", expand=True)

        # Botones de Acción (Confirmar, Cancelar, Editar)
        btns_detalles = tk.Frame(right_frame, bg="white")
        btns_detalles.pack(fill="x", pady=(10, 0))
        tk.Button(btns_detalles, text="Confirmar", bg="#5CFF5C", relief="flat", padx=10, command=self.confirmar_seleccionada).pack(side="left", padx=2,)
        tk.Button(btns_detalles, text="Cancelar", bg="#FF4C4C", fg="white", relief="flat", padx=10, command=self.cancelar_seleccionada).pack(side="left", padx=2)
        #tk.Button(btns_detalles, text="Editar", bg="#4CB5FF", fg="white", relief="flat", padx=10, command=self.editar_reserva).pack(side="left", padx=2)

        #  BOTÓN INFERIOR 
        btn_nueva = tk.Button(self, text="Agregar nueva reserva", bg="white", relief="flat",
                              highlightthickness=1, highlightbackground="#CCC",
                              font=("Segoe UI", 10), padx=15, pady=5,
                              command=self.abrir_nueva_reserva)
        btn_nueva.pack(anchor="w", padx=30, pady=20)

        self.tabla.bind("<<TreeviewSelect>>", self.on_reserva_seleccionada)

    # Método para manejar la selección de una reserva en la tabla y mostrar sus detalles.
    def on_reserva_seleccionada(self, event):
        seleccion = self.tabla.selection()
        if not seleccion: return
        
        indice = self.tabla.index(seleccion[0])
        reserva = self.controller.listar_reservas()[indice]
        
        # Actualizar panel derecho
        self.txt_detalles.config(text=reserva.mostrar_informacion(), fg="#333")

    # Método para confirmar la reserva seleccionada, actualizando su estado y refrescando la tabla y detalles.
    def confirmar_seleccionada(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione una reserva")
            return
    
        indice = self.tabla.index(seleccion[0])
        exito, msj = self.controller.confirmar_reserva(indice)
    
        if exito:
            messagebox.showinfo("Éxito", msj)
            self.cargar_reservas() # Refrescar tabla
            self.on_reserva_seleccionada(None) # Refrescar panel de detalles
        else:
            messagebox.showerror("Error", msj)

    # Método para cancelar la reserva seleccionada, actualizando su estado y refrescando la tabla y detalles.
    def cancelar_seleccionada(self):
        seleccion = self.tabla.selection()
        if not seleccion: return
        
        indice = self.tabla.index(seleccion[0])
        if messagebox.askyesno("Confirmar", "¿Desea cancelar esta reserva?"):
            exito, msj = self.controller.cancelar_reserva(indice)
            if exito:
                self.cargar_reservas()
                self.on_reserva_seleccionada(None)
            else:
                messagebox.showerror("Error", msj)

    # Método para abrir la vista de edición de reserva, pasando la reserva seleccionada y su índice.
    def editar_reserva(self):
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Seleccione una reserva para editar")
            return
        indice = self.tabla.index(seleccion[0])
        reserva = self.controller.listar_reservas()[indice]
        NuevaReservaView(self, self.controller, editar_reserva=reserva, indice_editar=indice)

    # Método para abrir la vista de nueva reserva, pasando el controlador para agregar la nueva reserva.
    def abrir_nueva_reserva(self):
        NuevaReservaView(self, self.controller)

    # Método para cargar las reservas desde el controlador y mostrarlas en la tabla, aplicando estilos según el estado.
    def cargar_reservas(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        reservas = self.controller.listar_reservas()

        for i, reserva in enumerate(reservas, start=1):
            self.tabla.insert(
                "",
                "end",
                values=(
                    i,
                    reserva.cliente.nombre,
                    reserva.servicio.nombre,
                    reserva.fecha,     
                    reserva.estado
                ),
                tags=(reserva.estado,) 
            )