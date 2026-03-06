from entidades.cliente import Cliente
from entidades.recibo import Recibo
from tarifa_enum import Tarifa
from datetime import datetime


print("escribe tu nombre")
nombre = input()

print("escribe tu direccion")
direccion = input()

c2 = Cliente(nombre, direccion, datetime.now())


print("cuantos kW gastaste")
gasto = float(input())


print("tipo de tarifa")
print("1 = domestico")
print("2 = empresarial")

tipo = int(input())

if tipo == 1:
    tarifa = Tarifa.DOMESTICO
else:
    tarifa = Tarifa.EMPRESARIAL


costo = Recibo(gasto, tarifa)

print(c2.nombre)
print(c2.direccion)
print(c2.fecha)


print("usted debe", costo.calcular_precio_total(), "pesos mexicanos")