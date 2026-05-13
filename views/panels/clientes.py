#importaciones necesarias para la interfaz gráfica y el controlador de clientes
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from controllers.cliente_controller import ClienteController

# Panel de gestión de clientes, con formulario para agregar nuevos clientes y tabla para listar los existentes.
class ClientesPanel(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        self.iconos = {}
        self.controller = ClienteController()
        self.crear_ui()
        self.cargar_clientes()
        
    #metodo para cargar iconos
    def _cargar_icono(self, nombre_archivo, size=(18, 18)):
        # CAMBIO: Ajustamos a la ruta correcta 'img/iconos/'
        try:
            img = Image.open(f"img/iconos_card/{nombre_archivo}.png").convert("RGBA")
            img = img.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            # Imprime el error para que sepas qué archivo falta exactamente
            print(f"Error cargando {nombre_archivo}: {e}")
            return None
        
    #metodo para crear la interfaz de usuario del panel de clientes
    def crear_ui(self):
        # TÍTULO
        tk.Label(self, text="Clientes", font=("Segoe UI", 22, "bold"), 
                 bg="white", fg="#333").pack(anchor="w", padx=30, pady=(10, 5))

        # FORMULARIO 
        #panel para agregar nuevos clientes
        form_frame = tk.LabelFrame(self, text="Agregar nuevo cliente:", font=("Segoe UI", 11, "bold"),
                                  bg="white", padx=20, pady=15, fg="#4C6EC0", relief="flat",
                                  highlightbackground="#DDD", highlightthickness=1)
        form_frame.pack(fill="x", padx=30, pady=10)

        #campos del formulario
        campos = [("Nombre:", "entry_nombre"), ("Teléfono:", "entry_tel"), ("E-mail:", "entry_mail")]
        self.entries = {}

        #creación de los campos del formulario
        for i, (label_text, var_name) in enumerate(campos):
            tk.Label(form_frame, text=label_text, font=("Segoe UI", 10), bg="white").grid(row=i, column=0, sticky="w", pady=2)
            ent = tk.Entry(form_frame, font=("Segoe UI", 11), highlightthickness=1, highlightbackground="#CCC", relief="flat")
            ent.grid(row=i, column=1, sticky="w", padx=10, pady=2, ipadx=40)
            self.entries[var_name] = ent

        #boton para agregar cliente
        btn_add = tk.Button(
            form_frame,
            text=" Agregar",
            bg="#5CFF5C",
            fg="black",
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            padx=20,
            cursor="hand2",
            command=self.agregar_cliente
        )
        btn_add.grid(row=3, column=0, columnspan=2, sticky="w", pady=(10, 0), ipady=3)

        # TABLA DE CLIENTES
        tabla_cont = tk.Frame(self, bg="white", highlightbackground="#EEE", highlightthickness=1) # panel para contener la tabla
        # expand=False y un height menor en el Treeview hacen la tabla más pequeña
        tabla_cont.pack(fill="both", expand=True, padx=30, pady=10)

        # Definimos las columnas de la tabla y configuramos su apariencia
        columnas = ("id", "nombre", "telefono", "email")
        # height=10 limita la tabla a 10 filas visibles inicialmente
        self.tabla = ttk.Treeview(tabla_cont, columns=columnas, show="headings", height=10)
        # Configuración de los encabezados y columnas   
        self.tabla.heading("id", text="ID")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("telefono", text="Teléfono")
        self.tabla.heading("email", text="E-mail")
        # Configuración de las columnas para que tengan un ancho adecuado y estén centradas
        self.tabla.column("id", width=50, anchor="center")
        self.tabla.column("nombre", width=200, anchor="center")
        self.tabla.column("telefono", width=120, anchor="center")
        self.tabla.column("email", width=180, anchor="center")

        self.tabla.pack(fill="both", expand=True) 

        #  BOTONES INFERIORES 
        footer_frame = tk.Frame(self, bg="white")
        footer_frame.pack(fill="x", padx=30, pady=(5, 15))
        self.iconos['details'] = self._cargar_icono("view") 

        #boton para ver detalles del cliente seleccionado
        btn_details = tk.Button(
            footer_frame, 
            text=" Ver detalles", 
            image=self.iconos.get('details'), 
            compound="left",
            bg="white", 
            relief="flat", 
            highlightthickness=1, 
            highlightbackground="#CCC",
            font=("Segoe UI", 9), 
            padx=15, 
            cursor="hand2",
            command=self.ver_detalles_cliente
        )
        btn_details.pack(side="left", ipady=5)

    # metodo para agregar un nuevo cliente utilizando el controlador
    def agregar_cliente(self):
        #obtener datos del formulario
        nombre = self.entries["entry_nombre"].get() 
        telefono = self.entries["entry_tel"].get() 
        email = self.entries["entry_mail"].get()

        #validar campos vacíos
        exito, mensaje = self.controller.registrar_cliente(
            nombre,
            email,
            telefono
        )

        #mostrar mensaje de éxito o error según el resultado de la operación
        if exito:
            messagebox.showinfo("Éxito", mensaje)
            self.limpiar_campos()
            self.cargar_clientes()
        else:
            messagebox.showerror("Error", mensaje)

    # metodo para cargar los clientes en la tabla
    def cargar_clientes(self):
        # Limpiar tabla antes de cargar nuevos datos
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        clientes = self.controller.listar_clientes() #obtener lista de clientes desde el controlador

        # Insertar clientes en la tabla con un ID visual (1, 2, 3...) para mostrar al usuario
        for i, cliente in enumerate(clientes, start=1):
            self.tabla.insert(
                "",
                "end",
                values=(
                    i,
                    cliente.nombre,
                    cliente.telefono,
                    cliente.email
                )
            )

    # metodo para mostrar detalles del cliente seleccionado en la tabla
    def ver_detalles_cliente(self):
        # Obtener item seleccionado
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Por favor, seleccione un cliente de la tabla")
            return

        # Obtener el índice del cliente seleccionado en la tabla para acceder a su información
        item_index = self.tabla.index(seleccion[0])
        cliente = self.controller.listar_clientes()[item_index]

        # Mostrar información detallada del cliente en un mensaje emergente
        info = cliente.mostrar_informacion()
        messagebox.showinfo("Información del Cliente", info)

    # metodo para limpiar los campos del formulario después de agregar un cliente
    def limpiar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)