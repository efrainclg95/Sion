"""Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta,
un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
Fruta         Precio
Plátano       1.35
Manzana       0.80
Pera          0.85
Naranja       0.70"""

def guarda_precio_dic(p_platano,p_manzana,p_pera,p_naranja):
    lista_frutas = ['Plátano','Manzana','Pera','Naranja']
    lista_precios = [p_platano,p_manzana,p_pera,p_naranja]
    dic_fruta_precio = dict(zip(lista_frutas,lista_precios))
    return dic_fruta_precio

print(guarda_precio_dic(1.35,0.80,0.85,0.70))