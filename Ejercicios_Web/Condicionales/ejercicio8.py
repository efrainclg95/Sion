v_puntuacion = float(input("Ingrese puntuacion del trabajador: "))
v_dinero = float(2.400)
v_total = float((v_puntuacion)*(v_dinero))

if(v_puntuacion == float("0.0")):
    print("Inaceptable, recibe S/. " + str(v_total))
elif(v_puntuacion >= float("0.1") and (v_puntuacion <= float("0.3"))):
    print("Puntuacion NV1")
elif(v_puntuacion == float("0.4")):
    print("Aceptable, recibe S/. " + str(v_total))
elif(v_puntuacion > float("0.4") and (v_puntuacion < float("0.6"))):
    print("Puntuacion NV2")
else:
    (v_puntuacion >= float("0.6"))
    print("Meritorio, recibe S/. " + str(v_total))



