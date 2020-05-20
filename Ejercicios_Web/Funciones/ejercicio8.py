# Escribir una función que reciba una muestra de números en una lista y
# devuelva un diccionario con su media, varianza y desviación típica.

lista = [1,2,3,4,5]
dic = {}

def f_media(lista):
    suma = 0
    for i in lista:
        suma += i
        media = suma / len(lista)
    return media

# print(f_media(lista))



dic['media'] = f_media(lista)


print(dic)

