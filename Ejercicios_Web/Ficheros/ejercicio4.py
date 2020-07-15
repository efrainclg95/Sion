"""Escribir un programa que acceda a un fichero de internet mediante su url
y muestre por pantalla el número de palabras que contiene."""

# Sol1

'''from urllib import request

def lectura_url(www):
    f = request.urlopen(www)
    datos = f.read()
    return datos.decode('utf-8')

def num_palabras(finter):
    contador_lista = finter.split()
    # print(contador_lista)
    return len(contador_lista)

# print(lectura_url('https://raw.githubusercontent.com/asalber/asalber.github.io/master/README.md'))
print(num_palabras(lectura_url('https://www.gutenberg.org/cache/epub/2000/pg2000.txt')))'''

# Sol2



