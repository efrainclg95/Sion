v_num = int(input("Ingrese un numero: "))

v_resto = int(v_num % 2)

print("resto es: " + str(v_resto))

if v_resto == 0:
    print(str(v_num) + " es par")
else:
    print(str(v_num) + " es impar")



