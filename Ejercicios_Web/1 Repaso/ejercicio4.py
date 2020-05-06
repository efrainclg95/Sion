# Escribir un programa que almacene las matrices:
# a = ((1,2,3),(4,5,6))
# b = ((-1,0),(0,1),(1,1))
# en una lista y muestre por pantalla su producto.
# Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.

a = ((1,2,3),(4,5,6))
b = ((-1,0),(0,1),(1,1))

la = []
lb = []

for i in range(len(a)):
    la.append(list(a[i]))

print(la)

# print(a[0])




