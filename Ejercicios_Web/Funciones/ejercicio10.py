# Escribir una función que convierta un número decimal en binario y
# otra que convierta un número binario en decimal.


# Estructurado

listab = [1,1,0,1,0]
listad = []

for i,j in enumerate(listab):

    cal = 2**i
    listab.reverse()

    oper = cal * listab[i]

    listad.append(oper)
    suma = sum(listad)

print(suma)


"""# A binario

n = 35

listai = []
listar = []

while n > 0:

    listai.append(n%2)
    n = n//2

for i in reversed(listai):
    listar.append(i)
print(listar)"""

# Funciones

"""def f_binario(n):
    listai = []
    listar = []

    while n>0:
        listai.append(n%2)
        n = n//2

    for i in reversed(listai):
        listar.append(i)

    return listar

print(f_binario(5))"""