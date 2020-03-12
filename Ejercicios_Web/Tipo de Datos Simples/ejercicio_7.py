v_horas = int(input("Ingrese horas de trabajo: "))
v_costo = float(input("Ingrese costo por hora de trabajo: "))

v_sueldo = float(v_horas * v_costo)*20

print("Horas ingresadas: {}".format(v_horas))
print("Costo por hora de trabajo: {}".format(v_costo))
print("Sueldo calculado es: {}".format(v_sueldo))
