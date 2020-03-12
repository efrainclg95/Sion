v_nombre = str(input("Ingresa tu nombre: "))
v_num_int = int(input("Ingresa un numero: "))


print(("Hola {}".format(v_nombre).upper()+"\n") * (v_num_int))
print(("Cantidad de letras del nombre ingresado es: ") + str(len(v_nombre)))