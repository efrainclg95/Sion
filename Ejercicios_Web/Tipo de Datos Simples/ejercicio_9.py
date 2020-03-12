v_peso = float(input("Ingrese su peso en Kg: "))
v_altura = float(input("Ingrese su altura en M: "))

v_imc = (v_peso)/(v_altura**2)
v_imc_redondeado = round(v_imc)

print(("Peso Ingresado es: {}").format(v_peso).upper()+" Kg")
print(("Altura Ingresada es: {}").format(v_altura).upper()+" m")

print(("Imc: {}").format(round(v_imc)).upper())

