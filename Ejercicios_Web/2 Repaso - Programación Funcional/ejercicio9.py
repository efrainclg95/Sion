"""Escribir un programa que gestione las facturas pendientes de cobro de una empresa.
Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura.
El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar.
Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario.
Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario.
Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro."""

# v_pregunta = str(input('Añadir una nueva factura (A)\nPagarla (P)\nTerminar (T)\nIngrese: '))
v_pregunta = str
dic = {}

def funcion0(v_pregunta):
    v_pregunta = str(input('Añadir una nueva factura (A)\nPagarla (P)\nTerminar (T)\nIngrese: '))
    return v_pregunta

def funcion1(v_pregunta):
    # funcion0(v_pregunta)
    while v_pregunta == 'A' or v_pregunta == 'P' or v_pregunta == 'T':
        if v_pregunta == 'A':
            v_num_factura = int(input('Introduce el número de la factura: '))
            v_coste_factura = float(input('Introduce el coste de la factura: '))
            dic[v_num_factura] = v_coste_factura
            return dic
        else:
            print('Sale del if')

    print('Sale de while')

print(funcion1(funcion0(v_pregunta)))


'''¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? A
Introduce el número de la factura: 01
Introduce el coste de la factura: 100
Diccionario temporal: {1: 100}
Recaudado: 0
Pendiente de cobro: 100
¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? A
Introduce el número de la factura: 02
Introduce el coste de la factura: 200
Diccionario temporal: {1: 100, 2: 200}
Recaudado: 0
Pendiente de cobro: 300
¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? P
Introduce el número de la factura a pagar: 02
Diccionario temporal borrado: {1: 100}
Recaudado: 200
Pendiente de cobro: 100'''