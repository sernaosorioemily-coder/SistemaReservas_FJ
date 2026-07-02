from modelos.entidad import Entidad
from modelos.excepciones import ClienteError

class Cliente(Entidad):

    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ClienteError("El nombre no puede estar vacío")
        self.__nombre = valor

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if "@" not in valor:
            raise ClienteError("Correo inválido")
        self.__correo = valor

    def mostrar_informacion(self):
        return f"{self.nombre} - {self.correo}"