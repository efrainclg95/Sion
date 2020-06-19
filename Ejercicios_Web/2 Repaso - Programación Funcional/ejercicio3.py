"""Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario
por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
Fruta         Precio
Plátano       1.35
Manzana       0.80
Pera          0.85
Naranja       0.70"""

p_platano = 1.35
p_manzana = 0.80
p_pera = 0.85
p_naranja = 0.70

fruta = str(input('Ingrese Fruta: '))
kilos = float(input('Ingrese la cantidad en Kilos: '))

def guarda_precio_dic(p_platano,p_manzana,p_pera,p_naranja):
    lista_frutas = ['Plátano','Manzana','Pera','Naranja']
    lista_precios = [p_platano,p_manzana,p_pera,p_naranja]
    dic_fruta_precio = dict(zip(lista_frutas,lista_precios))
    return dic_fruta_precio

def usuario(fruta,kilos):
    opera = guarda_precio_dic(p_platano,p_manzana,p_pera,p_naranja).get(fruta)*kilos
    cadena = str(opera),' Soles es el precio de ',fruta,' para llevar'
    cadena = ''.join(cadena) # convierte de tupla a cadena
    return cadena

print(usuario(fruta,kilos))



