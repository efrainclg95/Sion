# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia.
# Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def out_diccionario(cadena):
    global dic
    dic = {}
    lista = cadena.split()

    for j,k in enumerate(lista):
        contador = lista.count(lista[j])

        dic[k] = contador

    return dic


def out_tupla(cadena):

    l_maximo = []

    for keys,values in dic.items():
        l_maximo.append(values)
        maximo = max(l_maximo)

        if dic.get(keys) == maximo:
            tupla = (keys,dic.get(keys))

    return (tupla)

texto = 'Felipe es un niño hermoso y  es es bebito bello niño es'


print(out_diccionario(texto))

print(out_tupla(out_diccionario(texto)))