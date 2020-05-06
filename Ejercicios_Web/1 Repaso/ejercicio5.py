# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

t1 = (1,2,3)
t2 = (-1,1,2)
l1 = []
l2 = []
prod = 0

for i in t1:
    l1.append(i)
for j in t2:
    l2.append(j)

for n,k in enumerate(l1):
    prod = l1[n] * l2[n] + prod
print("Producto Escalar: " + str(prod))

