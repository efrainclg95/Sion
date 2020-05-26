# Escribir una función que convierta un número decimal en binario y
# otra que convierta un número binario en decimal.

"""n = 35

listai = []
listar = []

while n > 0:

    listai.append(n%2)
    n = n//2

for i in reversed(listai):
    listar.append(i)
print(listar)"""

def f_binario(n):
    listai = []
    listar = []

    while n>0:
        listai.append(n%2)
        n = n//2

    for i in reversed(listai):
        listar.append(i)

    return listar

print(f_binario(5))