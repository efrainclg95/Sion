# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia.
# Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

texto = 'Felipe es un niño hermoso y es bebito bello niño es'

dic = {}
lista = texto.split()

for j,k in enumerate(lista):
    contador = lista.count(lista[j])
    # print(k,contador)

    dic[k] = contador

print(dic)


for keys,values in dic.items():
    print(keys,values)
