"""Escribir una función que pida dos números n y m entre 1 y 10,
lea el fichero tabla-n.txt con la tabla de multiplicar de ese número,
y muestre por pantalla la línea m del fichero.
Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello."""

# Sol 1

"""n = int(input('Ingrese valor de n: '))
m = int(input('Ingrese valor de m: '))

archivo = 'tabla-' + str(n) + '.txt'

try:
    fichero = open(archivo,'r')
except FileNotFoundError:
    print('No existe tabla de multiplicar de:',n)
else:
    lista = fichero.readlines()
    print(lista[m-1])"""

# Sol 2

n = int(input('Ingrese valor de n: '))
m = int(input('Ingrese valor de m: '))

fn = 'Tabla-' + str(n) + '.txt'

try:
    f = open(fn,'r')
except FileNotFoundError:
    print('Fichero no existe')
else:
    print(f.read())

