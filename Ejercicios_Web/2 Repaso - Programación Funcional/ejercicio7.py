"""Escribir un programa que cree un diccionario simulando una cesta de la compra.
El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar.
Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato:
Lista de Compra
articulo1     Precio
articulo2     Precio
articulo3     Precio
Total         Costo"""

v_articulo = str(input('Que articulo desea comprar: '))
v_precio = float(input('Ingrese precio del artículo: '))

def f_dic_compras(v_articulo,v_precio):
    v_continua = 'Si'
    dic = {}
    while v_continua == 'Si':

        dic[v_articulo] = v_precio
        v_continua = str(input('Desea continuar con las compras (Si/No): '))
    return dic

print(f_dic_compras(v_articulo,v_precio))
