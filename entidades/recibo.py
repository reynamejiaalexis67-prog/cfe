
from tarifa_enum import Tarifa

class Recibo:

    def __init__(self, consumo_kw:float, tarifa:Tarifa):
        self.consumo_kw = consumo_kw
        self.tarifa = tarifa

    def calcular_precio_total(self):
        total = self.consumo_kw * self.tarifa.value
        return total


