f = open('virus.txt','w')
f.write('es un virus 11 pertenece a felipus ')

f = open('virus.txt','a')
f.write('\nno pertenece a efrain\nsi a karina')

f = open('virus.txt','r')
print(f.read())
f.close()



