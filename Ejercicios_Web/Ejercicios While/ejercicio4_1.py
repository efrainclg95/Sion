# Escriba un programa que pida la cantidad de números positivos que se tienen que escribir y a continuación pida números
# hasta que se haya escrito la cantidad de números positivos indicada.

########################################################################################################################
print("   XXXXXXXXX   NUMEROS POSITIVOS   XXXXXXXXX   ")

v_in_cantidad = int(input("Escriba la cantidad de números positivos a escribir: "))
v_contadorp = int(0)
v_contadorn = int(0)

while v_in_cantidad > 0:
    v_in_num = int(input("Escribe un numero: "))

    if v_in_num > 0:
        v_contadorp += 1
    else:
        v_contadorn += 1

    v_in_cantidad = v_in_cantidad - 1

print("Escribio " + str(v_contadorn) + " numeros negativos y " + str(v_contadorp) + " numeros positivos")

















