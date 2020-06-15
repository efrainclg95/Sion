"""Escribir una función que calcule el módulo de un vector."""

def modulo_vector(tupla):
    modulo = 0
    for i in tupla:
        modulo = modulo + i**2
    return modulo

print(modulo_vector((3,4)))