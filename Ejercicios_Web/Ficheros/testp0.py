f = open('virus_1','w')
f.write('Es un virus 1\n')

f = open('virus_1','a')
f.write('Felipe y sus padres aman a Dios')

f = open('virus_1','r')
print(f.read())

f.close()