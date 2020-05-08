# Escribir un programa que cree un diccionario de traducción español-inglés.
# El usuario introducirá las palabras en español e inglés separadas por dos puntos,
# y cada par <palabra>:<traducción> separados por comas.
# El programa debe crear un diccionario con las palabras y sus traducciones.
# Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra.
# Si una palabra no está en el diccionario debe dejarla sin traducir.

# v_palabra = str(input("Introduce la lista de palabras y traducciones en formato <<palabra:traducción>> separadas por comas: "))
v_palabra = 'perro:dog,bueno:good'
lista = v_palabra.split(',')
dic = {}

print(lista)

for i in lista:
    lista = i.split(':')
    print(lista)
    # dic = {i}
    # print(dic)

