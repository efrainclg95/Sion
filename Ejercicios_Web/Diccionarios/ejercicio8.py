# Escribir un programa que cree un diccionario de traducción español-inglés.
# El usuario introducirá las palabras en español e inglés separadas por dos puntos,
# y cada par <palabra>:<traducción> separados por comas.
# El programa debe crear un diccionario con las palabras y sus traducciones.
# Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra.
# Si una palabra no está en el diccionario debe dejarla sin traducir.

dic = {}
lista1 = []
lista2 = []
lista3 = []
# frase = str(input("Introduce la lista de palabras y traducciones en formato <<palabra:traducción>> separadas por comas:"))
frase = str("perro:dog,blanco:white,esta:its,jugando:playing")

lista1 = frase.split(',')
# print("lista1: " + str(lista1))

for i in range(len(lista1)):
    # lista2.append(lista1[i])
    lista2 = lista1[i].split(':')
    lista3.append(lista2[1])
    # print("lista3: " + str(lista3))
    # lista3.append(lista2[1])
    dic[lista2[0]] = lista2[1]
    # print("lista2: " + str(lista2))

print(dic)








