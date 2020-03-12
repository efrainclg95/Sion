# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares
# desde 1 hasta ese número separados por comas.

v_num = int(input("Ingrese un numero: "))
v_par = v_num % 2

if v_par == 0:
    print(str(v_num) + " es par" "\n")
    for i in range(v_num):
        i = i + 1
        v_par = i % 2
        if v_par == 0:
            print(str(i), end = ", ")

else:
    print(str(v_num) + " es impar" "\n")
    for i in range(v_num):
        i = i + 1
        v_par = i % 2
        if v_par != 0:
            print(str(i), end = ", ")






