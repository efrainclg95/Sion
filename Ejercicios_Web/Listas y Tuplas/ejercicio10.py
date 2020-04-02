# Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8,
# y muestre por pantalla el menor y el mayor de los precios.

# Sol1

# lprecios = [50,75,46,22,80,65,8]

# max = max(list(lprecios))
# min = min(list(lprecios))

# print("El mayor precio es: " + str(max))
# print("El menor precio es: " + str(min))

# Sol2

lprecios = [50,75,46,22,80,65,8,300,1]

for i in lprecios:
    # print(str(i))
    if i >= max(lprecios):
        print("El mayor es: " + str(i))
    elif i <= min(lprecios):
        print("El menor es: " + str(i))






