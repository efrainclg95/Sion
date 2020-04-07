# Escribir un programa que pregunte por una muestra de números, separados por comas,
# los guarde en una lista y muestre por pantalla su media y desviación típica.

v_num = input("Introduce una muestra de números separados por comas: ")
v_num = v_num.split()

for i in v_num:
    print("Valor de i: " + i)