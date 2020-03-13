# Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.

v_frase = str(input("Ingrese una frase: ").upper())
v_letra = str(input("Decida una letra: ").upper())

for i in (v_frase):
    # print(list(i))
    # print(str(i))
    # print(list(v_frase))
    if i == v_letra:
        print("COINCIDENCIA, La letra i es:  {}".format(v_letra))
    else:
        print(str(i) + ": No coincide con letra ingresada")
