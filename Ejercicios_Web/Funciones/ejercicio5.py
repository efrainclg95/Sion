# Escribir una función que calcule el área de un círculo y
# otra que calcule el volumen de un cilindro usando la primera función.

radio = float(input("Ingrese radio de circulo: "))

def area_circulo(radio):
    pi = 3.14159
    # radio = float(input("Ingrese radio de circulo: "))
    global v_acirculo
    v_acirculo = pi * radio**2
    # return 'Area de circulo: ' + str(v_acirculo)
    return 'Area de circulo: ' + str(v_acirculo)

print(area_circulo(radio))

h = int(input("Ingrese altura de cilindro: "))

def volumen_cilindro(h):

    v_cilindro = v_acirculo * h
    return 'Volumen de cilindro: ' + str(v_cilindro)

print(volumen_cilindro(h))
