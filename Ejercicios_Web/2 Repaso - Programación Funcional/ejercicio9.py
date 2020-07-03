"""Escribir un programa que gestione las facturas pendientes de cobro de una empresa.
Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura.
El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar.
Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario.
Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario.
Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro."""

dic = {}

def funcion1(respuesta):
    v_recaudo = 0
    while respuesta == 'A' or respuesta == 'P':
        respuesta = str(input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)?: '))
        if respuesta == 'A':
            v_n_factura = int(input('Ingrese # factura: '))
            v_c_factura = float(input('Ingrese costo de factura: '))
            dic[v_n_factura] = v_c_factura
            print(dic)

        elif respuesta == 'P':
            v_nf_pagar = int(input('Ingrese # factura a pagar: '))
            v_recaudo += dic.get(v_nf_pagar)
            print('Recaudado: ',v_recaudo)
            del dic[v_nf_pagar]
            print(dic)

        elif respuesta == 'T':
            return 'BYE'

print(funcion1('A'))
