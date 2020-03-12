v_edad = int(input("Ingrese la edad del cliente: "))

if v_edad < int(4):
    print("Ingresa Gratis")
elif v_edad >= int(4) and v_edad < int(18):
    print("Paga S/. 5")
elif v_edad >= int(18):
    print("Paga S/. 10")
else:
    print("Fin")
