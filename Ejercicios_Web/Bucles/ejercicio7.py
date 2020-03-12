# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

v_num = int(11)

for i in range(v_num):
    print("Tabla del: " + str(i))
    for j in range (v_num):
        print("Valor i: " + str(i) + " Valor j: " + str(j))
        print("Multiplicando el resultado es: " + str(i * j))
    print("")

