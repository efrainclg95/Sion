'''Escribir un programa que pregunte al usuario por las ventas de un rango de años y
muestre por pantalla una serie con los datos de las ventas indexada por los años,
antes y después de aplicarles un descuento del 10%.'''

import pandas as pd

v_inicial = int(input('Introduce el año incial: '))
v_final = int(input('Introduce el año final: '))

dic_ventas = {}

for i in range(v_inicial,v_final + 1):

    v_ventas_i = int(input('Introduce las ventas del año ' + str(i) + ': '))

    dic_ventas[i] = v_ventas_i

print(dic_ventas)






