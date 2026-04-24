from controllers.login_controller import LoginController
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk # Necesitarás: pip install Pillow
import ctypes
    
def centrar_ventana(v, w, h):
        v.update_idletasks()
        x = (v.winfo_screenwidth() // 2) - (w // 2)
        y = (v.winfo_screenheight() // 2) - (h // 2)
        v.geometry(f'{w}x{h}+{x}+{y}')

class LoginView:
    def __init__(self):
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except:
            pass
        
        # Configuración inicial
        self.controller = LoginController(self) # Descomentar cuando uses tu controlador
        self.ventana = tk.Tk()
        self.ventana.title("Login App")
        
        # Dimensiones basadas en la imagen (más ancha que alta)
        self.ancho = 900
        self.alto = 500
        centrar_ventana(self.ventana, self.ancho, self.alto)
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="white")

        self.crear_ui()
        self.ventana.mainloop()

    def crear_ui(self):
        # --- PANEL IZQUIERDO (Imagen) ---
        self.left_frame = tk.Frame(self.ventana, bg="white", width=self.ancho//2, height=self.alto)
        self.left_frame.pack(side="left", fill="both", expand=True)

        try:
            # Reemplaza 'imagen_login.png' con la ruta de tu imagen
            img_original = Image.open("img/login.png") 
            # Redimensionar manteniendo aspecto si es necesario
            img_res = img_original.resize((400, 350), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(img_res)
            
            self.lbl_img = tk.Label(self.left_frame, image=self.photo, bg="white")
            self.lbl_img.place(relx=0.5, rely=0.5, anchor="center")
        except:
            self.lbl_error = tk.Label(self.left_frame, text="[Ilustración]", bg="white", fg="#4C6EC0")
            self.lbl_error.place(relx=0.5, rely=0.5, anchor="center")

        # --- PANEL DERECHO (Formulario) ---
        # Color azul de fondo similar al de la imagen
        color_azul = "#4C6EC0" 
        self.right_frame = tk.Frame(self.ventana, bg=color_azul, width=self.ancho//2, height=self.alto)
        self.right_frame.pack(side="right", fill="both", expand=True)

        # Contenedor central para el formulario (para centrar verticalmente)
        self.form_container = tk.Frame(self.right_frame, bg=color_azul)
        self.form_container.place(relx=0.5, rely=0.5, anchor="center")

        # Textos de bienvenida
        tk.Label(self.form_container, text="Inicio de sesion", font=("Segoe UI", 28, "bold"), 
                 bg=color_azul, fg="white").pack(pady=(0, 5))
        
        # Campo: Username
        tk.Label(self.form_container, text="Username", font=("Segoe UI", 11), 
                 bg=color_azul, fg="white").pack(anchor="w", padx=40)
        self.entry_user = tk.Entry(self.form_container, font=("Segoe UI", 12), bd=0, highlightthickness=0)
        self.entry_user.pack(fill="x", padx=40, pady=(5, 15), ipady=8)

        # Campo: Password
        tk.Label(self.form_container, text="Password", font=("Segoe UI", 11), 
                 bg=color_azul, fg="white").pack(anchor="w", padx=40)
        self.entry_pass = tk.Entry(self.form_container, font=("Segoe UI", 12), show="*", bd=0, highlightthickness=0)
        self.entry_pass.pack(fill="x", padx=40, pady=(5, 5), ipady=8)

        # Opciones extras (Keep me logged in / Forgot Password)
        options_frame = tk.Frame(self.form_container, bg=color_azul)
        options_frame.pack(fill="x", padx=40, pady=5)
        
        # Botón Login (Estilo redondeado simulado con relief)
        btn_login = tk.Button(
            self.form_container, 
            text="Login", 
            command=self.login,
            bg="#7A96D6", # Un azul más claro para el botón
            fg="white", 
            font=("Segoe UI", 12, "bold"),
            bd=0,
            cursor="hand2",
            activebackground="#7289da"
        )
        btn_login.pack(fill="x", padx=40, pady=(30, 0), ipady=10)

    def login(self):
        self.controller.validar(
            self.entry_user.get(),
            self.entry_pass.get()
        )