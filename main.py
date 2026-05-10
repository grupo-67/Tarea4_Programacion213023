from views.loginview import LoginView
from views.layouts.main_layout import MainLayout

# Punto de entrada principal del programa.
# iniciando la interfaz de login del sistema.
if __name__ == "__main__":
    app = LoginView()
    app = MainLayout()
    app.mainloop()