from modelos.servicio import Servicio

class ReservaSala(Servicio):

    def calcular_costo(self, horas):
        return horas * self.tarifa

    def descripcion(self):
        return "Reserva de Salas"