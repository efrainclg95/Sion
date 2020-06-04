"""Escribir una función que simule una calculadora científica que permita calcular
el seno, coseno, tangente, exponencial y logaritmo neperiano.
La función preguntará al usuario el valor y la función a aplicar,
y mostrará por pantalla una tabla con los enteros de 1 al valor introducido
y el resultado de aplicar la función a esos enteros."""

from math import sin,cos,tan,exp,log

f = 'log'
n = 10

dic_trigo = {'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}
dic_resultado = {}

for i in range(1,10+1):
    dic_resultado[i] = dic_trigo[f](i)


for j in dic_resultado:
    print(j, '\t', dic_resultado.get(j))

