# Escribir un programa que cree un diccionario de traducción español-inglés.
# El usuario introducirá las palabras en español e inglés separadas por dos puntos,
# y cada par <palabra>:<traducción> separados por comas.
# El programa debe crear un diccionario con las palabras y sus traducciones.
# Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra.
# Si una palabra no está en el diccionario debe dejarla sin traducir.

# v_palabra = str(input("Introduce la lista de palabras y traducciones en formato <<palabra:traducción>> separadas por comas: "))
# v_frase = str(input("Introduce una frase para traducir: "))
v_palabra = 'perro:dog,bueno:good'
v_frase = 'el perro es bueno'
listap = v_palabra.split(',')
listaf = v_frase.split()
listat = []
dic = {}

for i in listap:
    listap = i.split(':')
    for n,k in enumerate(listap):
        dic[listap[0]] = k

        # print("Lista frase 0: " + str(listap))

print("Diccionario: " + str(dic))
print("Lista frase 1: " + str(listaf))

for n,m in enumerate(listaf):
    if m == 'perro':
        listaf[n] = 10
        print(listaf)

















