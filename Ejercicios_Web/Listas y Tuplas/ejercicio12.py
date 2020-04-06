# Escribir un programa que almacene las matrices:
# a = ((1,2,3),(4,5,6))
# b = ((-1,0),(0,1),(1,1))
# en una lista y muestre por pantalla su producto.
# Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.

a = ((1,2,3),(4,5,6))
b = ((-1,0),(0,1),(1,1))

result = [[0,0],
          [0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
for i in range(len(result)):
    result[i] = tuple(result[i])
result = tuple(result)
for i in range(len(result)):
    print(result[i])
