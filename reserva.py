from modelos.excepciones import ReservaError

class Reserva:

    def __init__(self, cliente, servicio, horas):

        self.cliente = cliente
        self.servicio = servicio
        self.horas = horas
        self.estado = "Pendiente"

    def confirmar(self):

        if self.horas <= 0:
            raise ReservaError("La duración debe ser mayor que cero")

        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"

    def procesar(self):
        return self.servicio.calcular_costo(self.horas)