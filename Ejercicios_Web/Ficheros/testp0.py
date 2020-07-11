'''f = open('virus_1','w')
f.write('Es un virus 1\n')

f = open('virus_1','a')
f.write('Felipe y sus padres aman a Dios')

f = open('virus_1','r')
print(f.read())

f.close()'''

import os
f = 'virus_1_1.txt'
if os.path.isfile(f):
    os.rename(f, 'virus_1_1.txt')
else:
    print('el fichero ',f,' no existe')

if os.path.isfile(f):
    os.remove(f)
else:
    print('el fichero ',f,' no existe')