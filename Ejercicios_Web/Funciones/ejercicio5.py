# Escribir una función que calcule el área de un círculo y
# otra que calcule el volumen de un cilindro usando la primera función.

# Sol 1

def area_circulo(r):
    pi = 3.14159
    return pi * r**2

def volumen_cilindro(r,h):
    return area_circulo(r)*h

print(area_circulo(80))
print(volumen_cilindro(80,500))


""""# Sol 2

radio = float(input("Ingrese radio de circulo: "))

def area_circulo(radio):
    pi = 3.14159
    global v_acirculo
    v_acirculo = pi * radio**2
    return 'Area de circulo: ' + str(v_acirculo)

print(area_circulo(radio))

h = int(input("Ingrese altura de cilindro: "))

def volumen_cilindro(h):

    v_cilindro = v_acirculo * h
    return 'Volumen de cilindro: ' + str(v_cilindro)

print(volumen_cilindro(h))"""
