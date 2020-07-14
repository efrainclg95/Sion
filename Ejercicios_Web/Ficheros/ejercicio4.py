"""Escribir un programa que acceda a un fichero de internet mediante su url
y muestre por pantalla el número de palabras que contiene."""

from urllib import request

def lectura_url(www):
    f = request.urlopen(www)
    datos = f.read()
    print(datos.decode('utf-8'))


print(lectura_url('https://raw.githubusercontent.com/asalber/asalber.github.io/master/README.md'))







'''palabras = 'hola amor de mi vida te amo mucho'

contador_lista = palabras.split()

print(len(contador_lista))'''