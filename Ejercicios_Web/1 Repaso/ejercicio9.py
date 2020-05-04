# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

v_contraseña = str("felipe")

while v_contraseña != "":
    v_password = str(input("Ingrese Contraseña: "))
    if v_password == v_contraseña:
        print("Contraseña Correcta BIENVENIDO")
    else:
        print("Contraseña Incorrecta")
