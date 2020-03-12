# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

v_login = str(input("Ingrese Contraseña: ").upper())
v_contrasena = str("cubo").upper()
v_intentos = int(4)

#Sol While

# while v_login != v_contrasena:
    # v_login = str(input("Ingrese Contraseña Nuevamente: ").upper())

# print("Contraseña Correcta :) :)")

#Sol For

for i in range(1,v_intentos):

    if v_login != v_contrasena:
        v_login = str(input("Intento " + str(i) + " Ingrese Contraseña Nuevamente: ").upper())
    else:
        print("Contraseña Correcta, Bienvenido")
        break













