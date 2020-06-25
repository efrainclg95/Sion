"""Escribir un programa que cree un diccionario de traducción español-inglés.
El usuario introducirá las palabras en español e inglés separadas por dos puntos,
y cada par <palabra>:<traducción> separados por comas.

El programa debe crear un diccionario con las palabras y sus traducciones.
Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra.
Si una palabra no está en el diccionario debe dejarla sin traducir."""

v_traductor = 'el:the,carro:car,papá:father,es:is'

def f_palabra(v_traductor):
    dic = {}
    lista2 = []
    lista1 = v_traductor.split(',')
    for i in lista1:
        lista2 = i.split(':')
        dic[lista2[0]] = lista2[1]
    return dic

def f_traduccion(v_frase):
    lista3 = v_frase.split()
    for n,k in enumerate(lista3):
        print(k)








print(f_palabra(v_traductor))
print(f_traduccion('el carro de papá es un volkswagen'))



