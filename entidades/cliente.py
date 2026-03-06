from datetime import datetime


class Cliente:

    def __init__(self, nombre:str, direccion:str, fecha:datetime):
        self.nombre = nombre
        self.direccion = direccion
        self.fecha = fecha
  