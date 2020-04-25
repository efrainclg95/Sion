# Escribir un programa que gestione las facturas pendientes de cobro de una empresa.
# Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura.
# El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar.
# Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario.
# Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario.
# Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

v_recaudado = int(0)
v_pendiente = int(0)
v_pregunta = str("A")
dic = {}

while v_pregunta == "A":
    v_pregunta = input("¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ")

    if v_pregunta == "A":
        v_numfac = int(input("Introduce el número de la factura: "))
        v_costfac = int(input("Introduce el coste de la factura: "))
        dic[v_numfac] = v_costfac
        print("Diccionario temporal: " + str(dic))

        v_pendiente += v_costfac

        print("Recaudado: " + str(v_recaudado))
        print("Pendiente de cobro: " + str(v_pendiente))

    elif v_pregunta == "P":
        v_pago = int(input("Introduce el número de la factura a pagar: "))

        v_recaudado = dic.get(v_pago)
        v_pendiente = v_pendiente - dic.get(v_pago)
        del dic[v_pago]

        print("Diccionario temporal borrado: " + str(dic))
        print("Recaudado: " + str(v_recaudado))
        print("Pendiente de cobro: " + str(v_pendiente))








