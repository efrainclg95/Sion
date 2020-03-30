# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

v_palabra = str(input("Ingrese palabra: "))

lista_x = []
lista_y = []

for i in v_palabra:
    lista_x.append(i)

print("lista_x: " + str(lista_x))

for j in range(len(v_palabra),0,-1):
    lista_y.append(v_palabra[j-1])

print("lista_y: " + str(lista_y))

if lista_x == lista_y:
    print("Es una palabra palíndromo")
else:
    print("No es un palíndromo")

# Python code to demonstrate working of
# reversed()

# For string
# seqString = "geeks"
# print(list(reversed(seqString)))

# For tuple
# seqTuple = ('g', 'e', 'e', 'k', 's')
# print(list(reversed(seqTuple)))

# For range
# seqRange = range(1, 5)
# print(list(reversed(seqRange)))

# For list
# seqList = [1, 2, 4, 3, 5]
# print(list(reversed(seqList)))