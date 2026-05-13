#importamos las librerias necesarias
import tkinter as tk
from PIL import Image, ImageTk

# Creamos la clase Sidebar que hereda de tk.Frame
class Sidebar(tk.Frame):
    #constructor de la clase Sidebar, recibe el padre y una función para manejar el cambio de navegación
    def __init__(self, parent, on_nav_change):
        super().__init__(parent, bg="#4C6EC0", width=220) # Establece un ancho fijo para la barra lateral
        self.pack_propagate(False)
        self.on_nav_change = on_nav_change
        self.iconos = {} # Diccionario para mantener las referencias de las imágenes (evita el Garbage Collector)
        self.crear_widgets()

    # Método privado para cargar y procesar los iconos de los botones
    def _cargar_icono(self, nombre_archivo, size=(20, 20)):
        # Carga una imagen, la redimensiona y la convierte a un formato compatible con Tkinter.
        try:
            ruta = f"img/iconos/{nombre_archivo}.png"
            img = Image.open(ruta).convert("RGBA")
            img = img.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error cargando icono {nombre_archivo}: {e}") # Manejo de errores al cargar la imagen
            return None

    # Método para crear los widgets de la barra lateral, incluyendo el logo y los botones de navegación
    def crear_widgets(self):
        # Logo o Texto Principal
        tk.Label(self, text="Software FJ", fg="white", bg="#4C6EC0", 
                 font=("Segoe UI", 20, "bold")).pack(pady=40)

        # Configuración de botones de navegación con sus respectivos iconos
        menu_items = [
            (" Inicio", "dashboard", "home"),
            (" Clientes", "clientes", "users"),
            (" Servicios", "servicios", "tools"),
            (" Reservas", "reservas", "calendar")
        ]

        # Iteramos sobre los elementos del menú para crear los botones correspondientes
        for texto, key, icono_name in menu_items:
            foto = self._cargar_icono(icono_name)
            if foto:
                self.iconos[key] = foto # Guardamos la referencia
            #botón de navegación con su respectivo texto e icono, además de estilos personalizados
            btn = tk.Button(
                self, 
                text=texto, 
                image=self.iconos.get(key), # Asignamos la imagen
                compound="left",            
                bg="#4C6EC0", 
                fg="white",
                font=("Segoe UI", 11), 
                relief="flat", 
                bd=0,
                padx=15,                    
                cursor="hand2", 
                activebackground="#1a1a3a", 
                activeforeground="white",
                command=lambda k=key: self.on_nav_change(k) # Llama a la función de cambio de navegación con la clave correspondiente al botón
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