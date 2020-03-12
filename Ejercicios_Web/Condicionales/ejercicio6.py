v_nombre = str(input("Ingrese Nombre: ").upper())
v_sexo = str(input("¿Cual es su Sexo? M/F: ").upper())

# Sol 1

# if (v_sexo == "M" and v_nombre >= "N") or (v_sexo == "F" and v_nombre <= "M"):
    # print("Perteneces al grupo A")
# else:
    # print("Perteneces al grupo B")

# Sol 2

if v_sexo == "M":
    if v_nombre > "O":
        print("Pertenece al grupo A")
    else:
        print("Pertenece al grupo B")
else:
    if v_sexo == "F":
        if v_nombre < "N":
            print("Pertenece al grupo A")
        else:
            print("Pertenece al grupo B")
print("Dato Incorrecto")
