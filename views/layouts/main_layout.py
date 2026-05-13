#importamos las librerias necesarias para la crecion de la interfaz principla del sistema
import tkinter as tk
from views.components.sidebar import Sidebar
from views.panels.dashboard import DashboardPanel
import ctypes
from controllers.main_controlller import MainController
from views.panels.clientes import ClientesPanel
from views.panels.servicio import ServiciosPanel
from views.panels.reservas import ReservasPanel

# Clase principal del layout del sistema, que contiene la barra lateral y el área de contenido dinámico.
class MainLayout(tk.Tk):
    def __init__(self):
        super().__init__() #Inicializamos la ventana principal
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1) #habilitar alta resolución en Windows
        except:
            pass
        self.title("Sistema de Gestión")
        self.geometry("1100x750")
        # Centrar ventana
        from utils.helpers import centrar_ventana
        centrar_ventana(self, 1100, 750)
        
        # Diccionario de paneles para evitar recrearlos (Opcional)
        self.paneles = {}
        self.main_controller = MainController() #controller principal
        
        # Contenedor para el contenido dinámico
        self.content_area = tk.Frame(self, bg="#F5F5F7")
        self.content_area.pack(side="right", fill="both", expand=True)

        # Sidebar
        self.sidebar = Sidebar(self, self.cambiar_panel)
        self.sidebar.pack(side="left", fill="y")

        # Cargar panel inicial
        self.cambiar_panel("dashboard")

    # Método para cambiar el panel de contenido según la selección en la barra lateral
    def cambiar_panel(self, key):
        # Limpiar el área de contenido
        for widget in self.content_area.winfo_children():
            widget.destroy()

        # sincronizamos los datos con el controlador principal antes de mostrar el panel
        clientes_db = self.main_controller.json_utils.cargar_clientes()
        servicios_db = self.main_controller.json_utils.cargar_servicios()

        # Actualizamos los controladores con los datos cargados
        self.main_controller.cliente_controller.clientes = clientes_db
        self.main_controller.servicio_controller.servicios = servicios_db
        self.main_controller.reserva_controller.reservas = self.main_controller.json_utils.cargar_reservas(
            clientes_db, servicios_db
        )

        # Seleccionar y mostrar el panel correspondiente
        if key == "dashboard": #dashboard del sistema, con resumen de clientes, servicios y reservas
            panel = DashboardPanel(self.content_area, self.main_controller) 
        elif key == "clientes": #panel de gestión de clientes, con opciones para agregar y visualizar clientes
            panel = ClientesPanel(self.content_area)
        elif key == "servicios": #panel de gestión de servicios, con opciones para agregar y visualizar servicios
            panel = ServiciosPanel(self.content_area)
        elif key == "reservas": #panel de gestión de reservas, con opciones para agregar y visualizar reservas
            panel = ReservasPanel(self.content_area,
                                  self.main_controller.reserva_controller)
        else:
            panel = tk.Label(self.content_area, text="En desarrollo...") #panel por defecto para opciones no implementadas
        panel.pack(fill="both", expand=True)