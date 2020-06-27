"""Escribir un programa que gestione las facturas pendientes de cobro de una empresa.
Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura.
El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar.
Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario.
Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario.
Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro."""




def funcion1(transa_A):
    dic = {}
    v_num_factura = int(input('Introduce el número de la factura: '))
    v_costo_factura = float(input('Introduce el coste de la factura: '))
    dic[v_num_factura] = v_costo_factura
    v_pendiente = 0
    v_pendiente += v_pendiente + dic.get(v_num_factura)
    print('Pendiente de cobro: ',v_pendiente)
    return dic

def funcion2(trans_P):
    v_num_factura_pagar = int(input('Introduce el número de la factura a pagar: '))
    v_recaudo = 0
    v_recaudo += funcion1('A').get(v_num_factura_pagar)
    return v_recaudo

print(funcion1('A'))
print(funcion2('P'))





