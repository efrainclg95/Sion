"""Escribir una función que calcule el módulo de un vector."""

import math

def modulo_vector(tupla):
    modulo = 0
    for i in tupla:
        modulo = modulo + i**2
    return math.sqrt(modulo)

print(modulo_vector((3,4,5)))