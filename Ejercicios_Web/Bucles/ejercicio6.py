# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo,
# de altura el número introducido.

v_num = int(input("Ingrese numero entero para la altura: "))

for i in range(v_num):
    for j in range(i + 1):
        print("*", end= " ")

    print("s")


