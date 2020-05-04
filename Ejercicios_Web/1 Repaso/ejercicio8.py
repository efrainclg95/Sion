# Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.

v_frase = str(input("Ingrese una frase: "))
v_letra = str(input("Escoja la letra: "))

# v_frase = str('Felipe el mejor')
# v_letra = str('e')
count = 0

for i in v_frase:
    if i == v_letra:
        count = count + 1

print("La letra: " + v_letra + " aparece: " + str(count) + " veces")

