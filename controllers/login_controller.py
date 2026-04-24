#importacion importante para el buen funcionamiento del controller login, usando el modelo o clase usuario y tkinter para el uso de alertas
from models.usser import Usuario
from tkinter import messagebox
from views.systemmain import systemmain

#clase login
class LoginController:
    #atributos de la clase
    def __init__(self, view):
        self.view = view
        self.usuario = Usuario()

    #funcion para validar y avisar al usuario si los datos ingresados con correcto o incorrectos
    def validar(self, user, password):
        if self.usuario.validar_usuario(user, password):
            messagebox.showinfo("Success", "Correct login")
            self.view.ventana.destroy()
            systemmain()
        else:
            messagebox.showerror("Error", "Incorrect data")