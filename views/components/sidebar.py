import tkinter as tk
from PIL import Image, ImageTk

class Sidebar(tk.Frame):
    def __init__(self, parent, on_nav_change):
        super().__init__(parent, bg="#4C6EC0", width=220)
        self.pack_propagate(False)
        self.on_nav_change = on_nav_change
        
        # Diccionario para mantener las referencias de las imágenes (evita el Garbage Collector)
        self.iconos = {}
        
        self.crear_widgets()

    def _cargar_icono(self, nombre_archivo, size=(20, 20)):
        """Método privado para procesar las imágenes de los iconos"""
        try:
            ruta = f"img/iconos/{nombre_archivo}.png"
            img = Image.open(ruta).convert("RGBA")
            img = img.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error cargando icono {nombre_archivo}: {e}")
            return None

    def crear_widgets(self):
        # Logo o Texto Principal
        tk.Label(self, text="Software", fg="white", bg="#4C6EC0", 
                 font=("Segoe UI", 20, "bold")).pack(pady=40)

        # Configuración de botones: (Texto, Key, Nombre_Archivo_Imagen)
        menu_items = [
            (" Inicio", "dashboard", "home"),
            (" Clientes", "clientes", "users"),
            (" Servicios", "servicios", "tools"),
            (" Reservas", "reservas", "calendar")
        ]

        for texto, key, icono_name in menu_items:
            # Cargar y guardar referencia del icono
            foto = self._cargar_icono(icono_name)
            if foto:
                self.iconos[key] = foto # Guardamos la referencia

            btn = tk.Button(
                self, 
                text=texto, 
                image=self.iconos.get(key), # Asignamos la imagen
                compound="left",            # Imagen a la izquierda del texto
                bg="#4C6EC0", 
                fg="white",
                font=("Segoe UI", 11), 
                relief="flat", 
                bd=0,
                padx=15,                    # Espaciado interno horizontal
                cursor="hand2", 
                activebackground="#1a1a3a", 
                activeforeground="white",
                command=lambda k=key: self.on_nav_change(k)
            )
            
            # Estilo de borde sutil
            btn.configure(highlightthickness=1, highlightbackground="#4C6EC0")
            btn.pack(fill="x", padx=25, pady=8, ipady=8)

        # Botón de Salida con su propio icono si deseas
        self.icono_exit = self._cargar_icono("logout")
        btn_exit = tk.Button(
            self, text=" Salir", image=self.icono_exit, compound="left",
            fg="#FF3333", bg="#4C6EC0", font=("Segoe UI", 11, "bold"), 
            relief="flat", highlightthickness=1, highlightbackground="#FF3333",
            command=self.quit
        )
        btn_exit.pack(side="bottom", fill="x", padx=25, pady=30, ipady=8)