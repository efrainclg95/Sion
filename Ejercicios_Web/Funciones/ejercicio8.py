# Escribir una función que reciba una muestra de números en una lista y
# devuelva un diccionario con su media, varianza y desviación típica.

# Sol 1

def square(sample):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    sample: Es una lista de números
    Devuelve una lista con los cuadrados de los números de la lista sample.
    """
    list = []
    for i in sample:
        list.append(i**2)
    return list

def statistics(sample):
    """Función que calcula la media, varianza y desviación típica de una muestra de números.
    Parámetros
    sample: Es una lista de números
    Devuelve un diccionario con la media, varianza y desviación típica de los números en sample.
    """
    stat = {}
    stat['media'] = sum(sample)/len(sample)
    stat['varianza'] = sum(square(sample))/len(sample)-stat['media']**2
    stat['desviacion tipica'] = stat['varianza']**0.5
    return stat

print(statistics([1, 2, 3, 4, 5]))
print(statistics([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))

# Sol 2

"""lista = [1,2,3,4,5]
lista_cuadrado = []
dic = {}

def cuadrado(lista):
    for i in lista:
        lista_cuadrado.append(i**2)
    return lista_cuadrado

# print("Lista cuadrado: " + str(cuadrado(lista)))

def f_media(lista):
    suma = 0
    for i in lista:
        suma += i
        media = suma / len(lista)
    return media

def f_varianza(lista):
    varianza = sum(cuadrado(lista))/len(lista) - dic['media']**2
    return varianza

def f_dtipica(lista):
    dtipica = dic['varianza']**0.5
    return dtipica

dic['media'] = f_media(lista)
dic['varianza'] = f_varianza(lista)
dic['desviacion tipica'] = f_dtipica(lista)

print(dic)"""

