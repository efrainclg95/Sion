v_cant_invertir = float(input("Ingrese cantidad a invertir : "))
v_interes = float(input("Ingrese interes anual : "))
v_anos = int(input("Ingrese el numero de años : "))

print("Capital obtenido es: " + str(round(v_cant_invertir * (v_interes / 100 + 1) ** v_anos, 1)))