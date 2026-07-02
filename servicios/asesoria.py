from modelos.servicio import Servicio

class Asesoria(Servicio):

    def calcular_costo(self, horas):
        return horas * self.tarifa * 1.20

    def descripcion(self):
        return "Asesoría Especializada"