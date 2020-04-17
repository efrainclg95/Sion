# Escribir un programa que cree un diccionario simulando una cesta de la compra.
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar.
# Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato:
# Lista de Compra
# articulo1     Precio
# articulo2     Precio
# articulo3     Precio
# Total         Costo

dic = {}
v_articulo = str(input("¿Qué artículo desea comprar? "))
v_precio = float(input("¿Cual es el precio? "))
dic[v_articulo] = v_precio
v_pregunta = str(input("¿Desea terminar con la lista? Si/No ").upper())

while v_pregunta == 'NO':

    v_articulo = str(input("¿Qué artículo desea comprar? "))
    v_precio = float(input("¿Cual es el precio? "))
    v_pregunta = str(input("¿Desea terminar con la lista? Si/No ").upper())
    dic[v_articulo] = v_precio

    print(dic)