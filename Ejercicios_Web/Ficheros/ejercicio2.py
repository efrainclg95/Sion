"""Escribir una función que pida un número entero entre 1 y 10,
lea el fichero tabla-n.txt con la tabla de multiplicar de ese número,
donde n es el número introducido, y la muestre por pantalla.
Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello"""

# Sol 1

n = int(input('Ingrese un número del 1 al 10: '))
nombre_archivo = 'tabla-' + str(n) + '.txt'

try:
    muestra = open(nombre_archivo,'r')
except FileNotFoundError:
    print('No existe el archivo con la tabla del #',n)

else:
    print(muestra.read())

# print(muestra.read())

# Sol 2

"""n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
try:
    f = open(file_name, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
else:
    print(f.read())"""