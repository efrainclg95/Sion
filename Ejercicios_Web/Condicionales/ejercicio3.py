v_n1 = float(input("Ingrese dividendo: "))
v_n2 = float(input("Ingrese divisor: "))
v_oper = float

if v_n2 == int(0):
    print("Error")
else:
    v_oper = v_n1/v_n2
    print("Resultado de la division es: " + str(v_oper))
    #print("Resultado de la division es: " + str(v_n1/v_n2))
