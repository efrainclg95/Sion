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

lista4 = []
lista5 = []

# palabra = str(input("Introduce la lista de palabras y traducciones en formato <<palabra:traducción>> separadas por comas:"))
palabra = str("perro:dog,blanco:white,esta:its,jugando:playing,casa:house")

lista1 = palabra.split(',')

for i in range(len(lista1)):
    lista2 = lista1[i].split(':')
    lista3.append(lista2[1])

    dic[lista2[0]] = lista2[1]

print(dic)
#print("lista2: " + str(lista2))
#print("lista3: " + str(lista3))

# frase = str(input("Ingrese frase: "))
frase = str("Mi Pibe el perro blanco esta jugando en la casa")
lista4 = frase.split()
# print(lista4)

for j in dic:
    # print("valor de j: " + j)
    for k in lista4:
        # print("valor de k: " + k)
        if j == k:
            lista5 = dic.get(j)
            print(lista5)
















