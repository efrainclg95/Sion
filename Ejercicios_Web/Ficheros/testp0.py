# creación escritura

'''f = open('bienvenido.txt','w')
f.write('Bienvenido a Python\n')'''

# añadiendo datos al fichero

'''f = open('bienvenido.txt','a')
f.write('Aprendamos a programar')'''

# leer datos de un fichero

'''f = open('bienvenido.txt','r')
print(f.read())'''

# cerrar un fichero

'''f = open('bienvenido.txt','r')
print(f.read())

f.close()'''

# renombrado de fichero

import os
'''os.rename('bienvenido.txt','hola.txt')'''

# renombrado comprobando existencia de fichero

'''f = 'hola3.txt'
if os.path.isfile(f):
    os.rename(f,'bienvenido.txt')
else:
    print('el fichero ' + f + ' no existe')'''


