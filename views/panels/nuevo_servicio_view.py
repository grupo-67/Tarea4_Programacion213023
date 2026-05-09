import tkinter as tk
from tkinter import ttk
import ctypes

class NuevoServicioView(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass
        self.title("Nuevo Servicio")
        self.geometry("450x500")
        self.configure(bg="white")
        # Centrar ventana usando tu helper
        from utils.helpers import centrar_ventana
        centrar_ventana(self, 450, 500)
        self.resizable(False, False)
        self.transient(parent) # Mantiene la ventana encima de la principal
        self.grab_set()        # Bloquea la ventana principal hasta cerrar esta

        self.crear_ui()

    def crear_ui(self):
        container = tk.Frame(self, bg="white", padx=20, pady=20)
        container.pack(fill="both", expand=True)

        tk.Label(container, text="Registrar Servicio", font=("Segoe UI", 14, "bold"), 
                 bg="white", fg="#4C6EC0").pack(pady=(0, 20))

        # --- TIPO DE SERVICIO (Selector Principal) ---
        tk.Label(container, text="Seleccione Tipo de Servicio:", bg="white").pack(anchor="w")
        self.combo_tipo = ttk.Combobox(container, values=["Sala", "Equipo", "Asesoria"], state="readonly")
        self.combo_tipo.pack(fill="x", pady=(5, 20))
        self.combo_tipo.bind("<<ComboboxSelected>>", self.actualizar_formulario)

        # --- ÁREA DINÁMICA ---
        # Este frame se limpiará y reconstruirá cada vez que cambie el combo
        self.dynamic_frame = tk.Frame(container, bg="white")
        self.dynamic_frame.pack(fill="both", expand=True)

        # Botón Guardar (inicialmente abajo)
        self.btn_guardar = tk.Button(container, text="Guardar Servicio", bg="#4C6EC0", fg="white",
                                     relief="flat", font=("Segoe UI", 10, "bold"), state="disabled")
        self.btn_guardar.pack(fill="x", pady=20, ipady=5)

    def actualizar_formulario(self, event):
        # Limpiar frame dinámico
        for widget in self.dynamic_frame.winfo_children():
            widget.destroy()
        
        tipo = self.combo_tipo.get()
        self.btn_guardar.config(state="normal")

        if tipo == "Sala":
            self.form_sala()
        elif tipo == "Equipo":
            self.form_equipo()
        elif tipo == "Asesoria":
            self.form_asesoria()

    def form_sala(self):
        tk.Label(self.dynamic_frame, text="Tipo de Sala:", bg="white").pack(anchor="w")
        ttk.Combobox(self.dynamic_frame, values=["Sala de Juntas", "Sala Audiovisual", "Biblioteca Virtual"], state="readonly").pack(fill="x", pady=5)
        
        tk.Label(self.dynamic_frame, text="Capacidad de personas:", bg="white").pack(anchor="w", pady=(10,0))
        tk.Entry(self.dynamic_frame).pack(fill="x", pady=5)
        
        tk.Label(self.dynamic_frame, text="Precio por hora:", bg="white").pack(anchor="w", pady=(10,0))
        tk.Entry(self.dynamic_frame).pack(fill="x", pady=5)

    def form_equipo(self):
        tk.Label(self.dynamic_frame, text="Tipo de Equipo:", bg="white").pack(anchor="w")
        ttk.Combobox(self.dynamic_frame, values=["Impresora", "Laptops"], state="readonly").pack(fill="x", pady=5)
        
        tk.Label(self.dynamic_frame, text="Precio por dia:", bg="white").pack(anchor="w", pady=(10,0))
        tk.Entry(self.dynamic_frame).pack(fill="x", pady=5)

    def form_asesoria(self):
        tk.Label(self.dynamic_frame, text="Especialidad:", bg="white").pack(anchor="w")
        ttk.Combobox(self.dynamic_frame, values=["Programacion", "Redes", "Diseño"], state="readonly").pack(fill="x", pady=5)
        
        tk.Label(self.dynamic_frame, text="Precio hora:", bg="white").pack(anchor="w", pady=(10,0))
        tk.Entry(self.dynamic_frame).pack(fill="x", pady=5)