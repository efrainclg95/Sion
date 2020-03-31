# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

vocales = ["a","e","i","o","u"]
v_palabra = str("karina")

for vocal in vocales:
    contador = 0
    for letra in v_palabra:
        if vocal == letra:
            contador = contador + 1
    print("la vocal " + str(vocal) + " se repite " + str(contador))








