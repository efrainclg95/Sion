'''Escribir un programa que pregunte al usuario por las ventas de un rango de años y
muestre por pantalla una serie con los datos de las ventas indexada por los años,
antes y después de aplicarles un descuento del 10%.'''

import pandas as pd

# Estructurado

'''v_inicial = int(input('Introduce el año incial: '))
v_final = int(input('Introduce el año final: '))

dic_ventas = {}

for i in range(v_inicial,v_final + 1):

    v_ventas_i = int(input('Introduce las ventas del año ' + str(i) + ': '))

    dic_ventas[i] = float(v_ventas_i)
    s = pd.Series(dic_ventas)

print('Ventas\n',s)
print('Ventas con descuento del 10%\n', s * 0.9)'''

# Funciones

dic_ventas = {}

def datos(inicial,final):

    for i in range(inicial,final + 1):
        v_ventas_i = int(input('Introduce las ventas del año ' + str(i) + ': '))

        dic_ventas[i] = float(v_ventas_i)
        s = pd.Series(dic_ventas)

    s1 = print('Ventas\n',s)
    s2 = print('Ventas con descuento\n', s * 0.9)

    return s1,s2

print(datos(2020,2021))













