v_contrasena = str("felipe").upper()
v_contrasenau = str(input("Ingrese contraseña de usuario: ").upper())

# print("la contraseña es: {}".format(v_contrasena))
print("la contraseña de usuario ingresada es: {}".format(v_contrasenau))

if v_contrasena == v_contrasenau:
    print("Bienvenido al reino de Dios")
else:
    print("Contraseña Incorrecta :( ")

