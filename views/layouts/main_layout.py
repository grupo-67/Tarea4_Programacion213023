import tkinter as tk
from views.components.sidebar import Sidebar
from views.panels.dashboard import DashboardPanel
import ctypes
from views.panels.clientes import ClientesPanel
from views.panels.servicio import ServiciosPanel
from views.panels.reservas import ReservasPanel

class MainLayout(tk.Tk):
    def __init__(self):
        super().__init__()
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass
        self.title("Sistema de Gestión")
        self.geometry("1100x750")

        # Centrar ventana usando tu helper
        from utils.helpers import centrar_ventana
        centrar_ventana(self, 1100, 750)
        
        # Diccionario de paneles para evitar recrearlos (Opcional)
        self.paneles = {}
        
        # Contenedor para el contenido dinámico
        self.content_area = tk.Frame(self, bg="#F5F5F7")
        self.content_area.pack(side="right", fill="both", expand=True)

        # Sidebar
        self.sidebar = Sidebar(self, self.cambiar_panel)
        self.sidebar.pack(side="left", fill="y")

        # Cargar panel inicial
        self.cambiar_panel("dashboard")

    def cambiar_panel(self, key):
        # Limpiar el área de contenido
        for widget in self.content_area.winfo_children():
            widget.destroy()

        # Selección de panel (SOLID: Podrías usar una Factory aquí si crece mucho)
        if key == "dashboard":
            panel = DashboardPanel(self.content_area)
        elif key == "clientes":
            panel = ClientesPanel(self.content_area)
        elif key == "servicios":
            panel = ServiciosPanel(self.content_area)
        elif key == "reservas":
            panel = ReservasPanel(self.content_area)
        else:
            panel = tk.Label(self.content_area, text="En desarrollo...")

        panel.pack(fill="both", expand=True)