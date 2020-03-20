# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

# v_ingresa_numeros = str(input("Ingrese los numeros ganadores: "))
v_lista_numeros = []

for i in range(1,8):
    v_ingresa_numeros = int(input("Ingresa Numero Ganador " + str(i) + ": " ))
    v_lista_numeros.append(v_ingresa_numeros)
print(sorted(v_lista_numeros))

