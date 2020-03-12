v_renta = int(input("Ingrese su renta anual: "))

#Sol1

#if v_renta <= int("10000"):
    #print("Su tipo de impositivo es de: 5% ")
#else:
    #if v_renta >= int("10001") and v_renta <= int("20000"):
        #print("Su tipo de impositivo es de: 15%")

#if v_renta >= int("20001") and v_renta <= int("35000"):
        #print("Su tipo de impositivo es de: 20%")
#else:
    #if v_renta >= int("35001") and v_renta <= int("60000"):
        #print("Su tipo de impositivo es de: 30%")

#if v_renta >= int("60001"):
    #print("Su tipo de impositivo es de: 45% ")

#Sol2

if v_renta <= int("10000"):
    print("Su tipo de impositivo es de: 5% ")
elif v_renta >= int("10001") and v_renta <= int("20000"):
    print("Su tipo de impositivo es de: 15% ")
elif v_renta >= int("20001") and v_renta <= int("35000"):
    print("Su tipo de impositivo es de: 20%")
elif v_renta >= int("35001") and v_renta <= int("60000"):
    print("Su tipo de impositivo es de: 30%")
else:
    v_renta >= int("60001")
    print("Su tipo de impositivo es de: 45% ")




