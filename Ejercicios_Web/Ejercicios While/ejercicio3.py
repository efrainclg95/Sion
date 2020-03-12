# Escriba un programa que pida números enteros mientras sean cada vez más grandes.

v_num1 = int(input("Escriba un numero: "))
v_num2 = int(input("Escriba un numero mayor que " + str(v_num1) + ": "))

while v_num2 > v_num1:
    v_num1 = v_num2
    v_num2 = int(input("Escriba un numero mayor que " + str(v_num1) + ": "))

print(str(v_num2) + " no es mayor que " + str(v_num1))