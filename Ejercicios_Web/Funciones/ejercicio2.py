# Escribir una función a la que se le pase una cadena <nombre> y muestre por pantalla el saludo ¡hola <nombre>!.

# Sol1

"""v_nombre = str(input("Ingrese un nombre: "))

def f_nombre():
    print("Hola " + v_nombre)

f_nombre()"""

# Sol2

def f_nombre(nombre):
    print("¡Hola " + nombre + "!")
    return

f_nombre('Felipe bebe')