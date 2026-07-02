from abc import ABC, abstractmethod
from modelos.excepciones import ServicioError

class Servicio(ABC):

    def __init__(self, nombre, tarifa):

        if tarifa <= 0:
            raise ServicioError("La tarifa debe ser mayor a cero")

        self.nombre = nombre
        self.tarifa = tarifa

    @abstractmethod
    def calcular_costo(self, horas):
        pass

    @abstractmethod
    def descripcion(self):
        pass

    def calcular_total(self, horas, impuesto=0, descuento=0):
        return self.calcular_costo(horas) + impuesto - descuento