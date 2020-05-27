# Escribir una función que reciba una muestra de números en una lista y devuelva su media.

# Sol1

"""lista = []

def media(lista):
    return sum(lista)/len(lista)

print(media([1,2,3]))"""

# Sol2

# lista = [1,2,3,4]

def f_media(lista):

    suma = 0

    for i in lista:

        suma = suma + i
        prom = suma/len(lista)

    print('suma: ', str(suma))

    return prom


print(f_media([1,2,5]))
