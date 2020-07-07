"""Escribir una función que pida un número entero entre 1 y 10
y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número,
donde n es el número introducido."""

# Sol 1

def input_num(n):

    file_name = 'tabla-' + str(n) + '.txt'
    f = open(file_name, 'w')

    for i in range(1,13):
        tabla = i * n
        # print(n,' x ',i, ' = ',tabla)
        f.write(str(n) + ' x ' + str(i) + ' = ' + str(tabla) + '\n')
    f.close()

print(input_num(int(input('Ingrese Número del 1 al 10: '))))

# Sol 2

"""n = int(input('Introduce un número entero entre 1 y 10: '))
file_name = 'tabla-' + str(n) + '.txt'
f = open(file_name, 'w')
for i in range(1, 11):
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
f.close()"""