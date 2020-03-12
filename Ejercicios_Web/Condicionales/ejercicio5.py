v_edad = int(input("Ingrese su edad: "))
v_edadlim = 16
v_ingreso = int(input("Ingrese sus ingresos S/.: "))

if v_edad >= v_edadlim and v_ingreso >= 1000:
    print("Tiene que pagar sus tributos")
else:
    print("Ud no paga nada")