# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.

v_num = int(input("Ingrese un número para la altura: "))

for i in range(1,v_num,2):
    for j in range(i,0, - 2):
        print(str(j), end=" ")
    print("a")
print("b")