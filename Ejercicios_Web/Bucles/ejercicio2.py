# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
v_in_edad = int(input("Ingrese su edad: "))

for i in range(v_in_edad):
    print("Usted cumplio: " + str(i + 1))