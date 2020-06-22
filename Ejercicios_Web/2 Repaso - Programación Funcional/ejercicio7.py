"""Escribir un programa que cree un diccionario simulando una cesta de la compra.
El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar.
Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato:
Lista de Compra
articulo1     Precio
articulo2     Precio
articulo3     Precio
Total         Costo"""

print('LISTA DE COMPRAS')

v_articulo = str
v_precio = float

def f_dic_compras(v_articulo,v_precio):
    v_continua = 'Si'
    dic = {}
    while v_continua == 'Si':
        v_articulo = str(input('Que articulo desea comprar: '))
        v_precio = float(input('Ingrese precio del artículo: '))
        dic[v_articulo] = v_precio
        v_continua = str(input('Desea continuar con las compras (Si/No): '))
    return dic

def f_costo(diccionario):
    v_total = 0
    for keys,values in diccionario.items():
        v_total += values
        cadena = 'Total de compras S/.: ',str(v_total)
        cadena = ''.join(cadena)
    return cadena

print(f_costo(f_dic_compras(v_articulo,v_precio)))

