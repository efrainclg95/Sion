# Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.

# Sol 1

v_frase = str(input("Ingrese una frase: ").upper())
v_letra = str(input("Decida una letra: ").upper())
count = int(0)

for i in (v_frase):

    if i == v_letra:
        count = count + 1

if count == 1:
    print("Se repite una vez")
else:
    print("Se repite {}".format(count) + " veces")

# Sol 2

# frase = input("Introduce una frase: ")
# letra = input("Introduce una letra")
# contador = 0
# for i in frase:
    # if i == letra:
        # contador += 1
# print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))











