# Escriba un programa que pida números decimales mientras el usuario escriba número mayores que el primero.

v_num1 = float(input("escribe un numero: "))
v_num2 = float(input("escribe un numero mayor a " + str(v_num1) + ": "))

while v_num1 >= v_num2:
    print(str(v_num2) + " no es mayor que " + str(v_num1))
    v_num2 = float(input("escribe otro numero mayor que " + str(v_num1) + ": "))

v_num2 = float(input("escribe otro numero mayor que " + str(v_num1) + ": "))
while v_num2 >= v_num1:
    v_num2 = float(input("escribe otro numero mayor que " + str(v_num1) + ": "))

print(str(v_num2) + " es mayor que " + str(v_num1))