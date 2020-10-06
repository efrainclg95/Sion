# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

lista = [1,2,3,4]

def f_lista_cuadrado(lista):
    # lista = []
    lc = []
    for i in lista:
        print(i)
        lc.append(i**2)

    return lc

print(f_lista_cuadrado([3,4]))

