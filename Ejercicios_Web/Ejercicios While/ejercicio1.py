# Escriba un programa que pida dos números enteros. El programa pedirá de nuevo el segundo número mientras no sea mayor que el primero.
# El programa terminará escribiendo los dos números.

v_num1 = int(input("Ingrese Primer Numero: "))
v_num2 = int(input("Ingrese Segundo Numero Mayor que " + str(v_num1) + ":" ))

while v_num1 > v_num2:
    print(str(v_num2) + " no es mayor que: " + str(v_num1))
    v_num2 = int(input("Vuelve a Ingresar Segundo Numero Mayor que " + str(v_num1) + ":" ))

print(str(v_num2) + " es mayor que: " + str(v_num1))
print("Los numeros ingresados son: " + str(v_num1) + " y " + str(v_num2))

