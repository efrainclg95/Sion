# Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.

v_frase = str(input("Ingrese una frase: ").upper())
v_letra = str(input("Decida una letra: ").upper())
count = int(0)

# Sol 1

for i in (v_frase):

    if i == v_letra:
        count = count + 1

if count == 1:
    print("Se repite una vez")
else:
    print("Se repite {}".format(count) + " veces")







