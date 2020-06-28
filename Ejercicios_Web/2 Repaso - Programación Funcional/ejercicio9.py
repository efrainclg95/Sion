"""Escribir un programa que gestione las facturas pendientes de cobro de una empresa.
Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura.
El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar.
Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario.
Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario.
Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro."""

v_pregunta = str(input('F1 Añadir una nueva factura (A)\nPagarla (P)\nTerminar (T)\nIngrese: '))

# while v_pregunta == 'A' or v_pregunta == 'P' or v_pregunta == 'T':
    # print('True')

def funcion1(v_pregunta):
    while v_pregunta == 'A' or v_pregunta == 'P' or v_pregunta == 'T':
        return v_pregunta


print(funcion1(v_pregunta))

'''v_pregunta = ''

def funcion1(v_pregunta):

    v_pregunta = str(input('F1 Añadir una nueva factura (A)\nPagarla (P)\nTerminar (T)\nIngrese: '))
    return v_pregunta

def funcion2(b_bucle):

    if funcion1(v_pregunta) == 'A':
        print('True A')
    elif funcion1(v_pregunta) == 'P':
        print('True P')
    elif funcion1(v_pregunta) == 'T':
        print('True T')

# print(funcion1(v_pregunta))
print(funcion2('b_bucle'))'''
