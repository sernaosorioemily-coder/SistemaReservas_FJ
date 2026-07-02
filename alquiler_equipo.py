from modelos.servicio import Servicio

class AlquilerEquipo(Servicio):

    def calcular_costo(self, horas):
        return horas * self.tarifa * 1.10

    def descripcion(self):
        return "Alquiler de Equipos"