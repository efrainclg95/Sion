"""Escribir una función que pida un número entero entre 1 y 10
y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número,
donde n es el número introducido."""

# Sol 1

"""def input_num(n):

    file_name = 'tabla-' + str(n) + '.txt'
    f = open(file_name, 'w')

    for i in range(1,13):
        tabla = i * n
        f.write(str(n) + ' x ' + str(i) + ' = ' + str(tabla) + '\n')
    f.close()

print(input_num(int(input('Ingrese Número del 1 al 10: '))))"""

# Sol 2

"""n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
f = open(file_name, 'w')
for i in range(1, 11):
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
f.close()"""

# Sol 3

def n_entero(n):

    fn = 'Tabla-' + str(n) + '.txt'
    f = open(fn,'w')

    for i in range(1,11):
        producto = n * i
        f.write(str(n) + ' x ' + str(i) + ' = ' + str(producto) + '\n')
    f.close()

def n_open(Tabla):

    f = open(Tabla,'r')
    print(f.read())

# print(n_entero(int(input('Ingrese un número entero: '))))
print(n_open('Tabla-12.txt'))