"""Escribir un programa que cree un diccionario de traducción español-inglés.
El usuario introducirá las palabras en español e inglés separadas por dos puntos,
y cada par <palabra>:<traducción> separados por comas.

El programa debe crear un diccionario con las palabras y sus traducciones.
Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra.
Si una palabra no está en el diccionario debe dejarla sin traducir."""

# v_palabra = str(input('Ingrese palabras <palabra>:<traducción>: '))
v_palabra = 'el:the,carro:car,papá:father'

def f_palabra(v_palabra):
    dic = {}
    lista2 = []
    lista1 = v_palabra.split(',')
    for i in lista1:
        lista2 = i.split(':')
        dic[i[0]] = i[1]
    print(dic)


print(f_palabra(v_palabra))



