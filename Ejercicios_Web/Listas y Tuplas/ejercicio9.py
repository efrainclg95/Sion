# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

vocales = ["a","e","i","o","u"]
v_palabra = str("karina")
contador = int(0)

for i in vocales:
    # print("vocal " + str(i))
    contador = 0
    for j in v_palabra:
        # print("palabra " + str(j))
        if i == j:
            contador = contador + 1

    print("la vocal: " + i + " se repite: " + str(contador) + " veces")








