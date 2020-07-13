fichero = open('virus.txt','w')
fichero.write('es un virus\n')

fichero = open('virus.txt','a')
fichero.write('creado por felipe')

fichero = open('virus.txt','r')
print(fichero.read())

fichero.close()

