# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

v_palabra = str(input("Ingrese una palabra: "))

# Solución 1
# for i in [0,1,2,3,4,5,6,7,8,9]:
    # print(str(v_palabra))

# Solución 2
for i in range(10):
    print("i: " + str(i) + " " + str(v_palabra))


