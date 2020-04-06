# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva,
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

# Sol1
# v_lista_numeros = []

# for i in range(1,8):
    # v_ingresa_numeros = int(input("Ingresa Numero Ganador " + str(i) + ": " ))
    # v_lista_numeros.append(v_ingresa_numeros)
# print(sorted(v_lista_numeros))

# Sol2 con números aleatorios

from random import randint

v_lista_bolas = []

for i in range(1,8):
    v_num = int(randint(0,50))
    print("Bola " + str(i) + ": " + str(v_num))
    v_lista_bolas.append(v_num)
print("Números Ganadores: " + str(v_lista_bolas))






