#importamos los comportamiento heredados de la clase padre Servicio
from models.servicio import Servicio

# La clase ServicioAsesoria representa un servicio de asesoría con una especialidad específica.
class ServicioAsesoria(Servicio):
    # El constructor de la clase ServicioAsesoria recibe la especialidad y el precio base del servicio.
    def __init__(self, especialidad, precio_base):
        super().__init__("Asesoría", precio_base) # llamamos al constructor de la clase padre
        #definimos el tipo de servicio como "asesoria" y asignamos la especialidad al atributo correspondiente.
        self.tipo = "asesoria"
        self._nombre = especialidad
        self.especialidad = especialidad

    #metodo para calcular el costo total
    def calcular_costo(self, duracion):
        return self._precio_base * duracion
    #metodo para describir el servicio, mostrando la especialidad y el precio base
    def describir_servicio(self):
        return f"Asesoría en {self.especialidad}\nPrecio: {self.precio_base}$"