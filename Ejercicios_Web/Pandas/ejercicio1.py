'''Escribir un programa que pregunte al usuario por las ventas de un rango de años y
muestre por pantalla una serie con los datos de las ventas indexada por los años,
antes y después de aplicarles un descuento del 10%.'''

import pandas as pd

v_inicial = int(input('Introduce el año incial: '))
v_final = int(input('Introduce el año final: '))

for i in range(v_inicial,v_final + 1):
    print(i)