import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from controllers.main_controlller import MainController

class DashboardPanel(tk.Frame):
    def __init__(self, parent, main_controller):
        super().__init__(parent, bg="white")
        self.main_controller = main_controller
        self.iconos = {}
        self.crear_ui()
        self.cargar_dashboard()


    def _cargar_icono(self, nombre_archivo, size=(50, 50)):
        try:
            # Ajusta la ruta según tu carpeta 'img/iconos/'
            img = Image.open(f"img/iconos_card/{nombre_archivo}.png").convert("RGBA")
            img = img.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error cargando {nombre_archivo}: {e}")
            return None

    def crear_ui(self):
        # --- TÍTULO ---
        tk.Label(self, text="Bienvenido", font=("Segoe UI", 22, "bold"), 
                 bg="white", fg="#333").pack(anchor="w", padx=30, pady=(20, 10))
        
        # --- CONTENEDOR DE CARDS (Indicadores) ---
        cards_frame = tk.Frame(self, bg="white")
        cards_frame.pack(fill="x", padx=25)
        """
        stats = [
            ("15", "Clientes", "Total registrados", "users_card"),
            ("9", "Servicios", "Disponibles", "services_card"),
            ("7", "Reservas", "Pendientes", "pending_card"),
            ("12", "Reservas", "Confirmadas", "check_card")
        ]"""
        self.cards_frame = cards_frame
        """
        for i, (val, tit, sub, icon_name) in enumerate(stats):
            foto = self._cargar_icono(icon_name)
            if foto: self.iconos[icon_name] = foto
            
            card = self._crear_card(cards_frame, val, tit, sub, self.iconos.get(icon_name))
            card.grid(row=0, column=i, padx=8, pady=10, sticky="nsew")
            cards_frame.columnconfigure(i, weight=1)
        """
        # --- SECCIÓN DE TABLA ---
        tk.Label(self, text="Ultimas Reservas:", font=("Segoe UI", 12, "bold"), 
                 bg="white", fg="#555").pack(anchor="w", padx=30, pady=(20, 5))
        
        # Contenedor para la tabla con un borde ligero
        tabla_frame = tk.Frame(self, bg="white", highlightbackground="#EEE", highlightthickness=1)
        tabla_frame.pack(fill="both", expand=True, padx=30, pady=10)

        columnas = ("id", "cliente", "servicio", "estado")
        self.tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings")
        
        # Estilo de la Tabla
        style = ttk.Style()
        style.theme_use("clam") # 'clam' permite personalizar mejor los colores en Tkinter
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#F9F9F9", relief="flat")
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=35, borderwidth=0)
        style.map("Treeview", background=[('selected', '#4C6EC0')])

        # Definir encabezados
        self.tabla.heading("id", text="ID")
        self.tabla.heading("cliente", text="Cliente")
        self.tabla.heading("servicio", text="Servicio")
        self.tabla.heading("estado", text="Estado")

        # Ajustar ancho de columnas
        self.tabla.column("id", width=100, anchor="center")
        self.tabla.column("cliente", width=250, anchor="w")
        self.tabla.column("servicio", width=200, anchor="w")
        self.tabla.column("estado", width=150, anchor="center")

        self.tabla.pack(fill="both", expand=True)

        # --- BOTONES INFERIORES ---
        btns_frame = tk.Frame(self, bg="white")
        btns_frame.pack(fill="x", padx=30, pady=(10, 25))

        # Cargamos iconos pequeños para los botones
        self.iconos['refresh'] = self._cargar_icono("refresh", (16, 16))
        self.iconos['view'] = self._cargar_icono("view", (16, 16))

        btn_refresh = tk.Button(btns_frame,
            text=" Actualizar",
            image=self.iconos.get('refresh'),
            compound="left",
            bg="white",
            relief="flat",
            highlightthickness=1,
            highlightbackground="#CCC",
            font=("Segoe UI", 9),
            padx=15,
            cursor="hand2",
            command=self.cargar_dashboard
        )
        btn_refresh.pack(side="left", padx=(0, 10), ipady=5)

        btn_view = tk.Button(
            btns_frame, text=" Ver datos", image=self.iconos.get('view'), 
            compound="left", bg="white", relief="flat", 
            highlightthickness=1, highlightbackground="#CCC",
            font=("Segoe UI", 9), padx=15, cursor="hand2"
        )
        btn_view.pack(side="left", ipady=5)

    def _crear_card(self, parent, valor, titulo, subtitulo, imagen):
        # Frame principal de la card con borde sutil
        f = tk.Frame(parent, bg="white", highlightbackground="#E0E0E0", highlightthickness=1)
        
        # Padding interno
        inner = tk.Frame(f, bg="white", padx=15, pady=20)
        inner.pack(fill="both", expand=True)

        # Lado Izquierdo: Icono
        if imagen:
            lbl_img = tk.Label(inner, image=imagen, bg="white")
            lbl_img.pack(side="left", padx=(0, 15))

        # Lado Derecho: Textos
        txt_cont = tk.Frame(inner, bg="white")
        txt_cont.pack(side="left", fill="both", expand=True)

        tk.Label(txt_cont, text=valor, font=("Segoe UI", 18, "bold"), 
                 bg="white", fg="#1A1A1A", anchor="w").pack(fill="x")
        
        tk.Label(txt_cont, text=titulo, font=("Segoe UI", 10, "bold"), 
                 bg="white", fg="#333", anchor="w").pack(fill="x")
        
        tk.Label(txt_cont, text=subtitulo, font=("Segoe UI", 8), 
                 bg="white", fg="#8E94A0", anchor="w").pack(fill="x")
        
        return f
    def cargar_dashboard(self):

        clientes = self.main_controller.cliente_controller.listar_clientes()
        servicios = self.main_controller.servicio_controller.listar_servicios()
        reservas = self.main_controller.reserva_controller.listar_reservas()

        pendientes = len([
            r for r in reservas
            if r.estado == "Pendiente"
        ])

        confirmadas = len([
            r for r in reservas
            if r.estado == "Confirmada"
        ])

        stats = [
            (
                len(clientes),
                "Clientes",
                "Total registrados",
                "users_card"
            ),
            (
                len(servicios),
                "Servicios",
                "Disponibles",
                "services_card"
            ),
            (
                pendientes,
                "Reservas",
                "Pendientes",
                "pending_card"
            ),
            (
                confirmadas,
                "Reservas",
                "Confirmadas",
                "check_card"
            )
        ]

        for widget in self.cards_frame.winfo_children():
            widget.destroy()

        for i, (val, tit, sub, icon_name) in enumerate(stats):

            foto = self._cargar_icono(icon_name)

            if foto:
                self.iconos[icon_name] = foto

            card = self._crear_card(
                self.cards_frame,
                str(val),
                tit,
                sub,
                self.iconos.get(icon_name)
            )

            card.grid(
                row=0,
                column=i,
                padx=8,
                pady=10,
                sticky="nsew"
            )

            self.cards_frame.columnconfigure(
                i,
                weight=1
            )

        self.cargar_tabla()

    def cargar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        reservas = self.main_controller.reserva_controller.listar_reservas()

        ultimas = reservas[-5:]

        for i, reserva in enumerate(ultimas, start=1):

            self.tabla.insert(
                "",
                "end",
                values=(
                    i,
                    reserva.cliente.nombre,
                    reserva.servicio.nombre,
                    reserva.estado
                )
            )