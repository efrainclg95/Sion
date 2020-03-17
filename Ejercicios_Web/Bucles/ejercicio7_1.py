# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

v_tabla = int(input("Que tabla de multiplicar desea ver: "))
v_num = 12

for i in range((v_tabla ),(v_tabla + 1)):
    for j in range(v_num + 1):
        print("Valor de I: {} Valor de J: {}".format(i,j) + " Multiplicado es: " + str(i * j))
    print("fin J")
print("fin I")
