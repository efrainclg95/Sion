# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

v_palabra = input("Introduce una palabra: ")

for i in range(len(v_palabra)-1, -1, -1):
    print(v_palabra[i])