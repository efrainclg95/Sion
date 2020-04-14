# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta,
# un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
# Fruta         Precio
# Plátano       1.35
# Manzana       0.80
# Pera          0.85
# Naranja       0.70

# Sol1

# v_fruta = str(input("Escriba que fruta desea comprar: "))
# v_kilos = int(input("Cuantos kilos desea llevar: "))
# dic = {'Plátano' : 1.35, 'Manzana' : 0.80, 'Pera' : 0.85, 'Naranja' : 0.70}

# print("Va a llevar: " + v_fruta + " " + str(v_kilos) + " Kilos, un total de: " + str(dic.get(v_fruta)*v_kilos))

# Sol2

v_fruta = str(input("Escriba que fruta desea comprar: "))
v_kilos = int(input("Cuantos kilos desea llevar: "))
dic = {'Plátano' : 1.35, 'Manzana' : 0.80, 'Pera' : 0.85, 'Naranja' : 0.70}

if v_fruta in dic:
    print("Va a llevar: " + v_fruta + " " + str(v_kilos) + " Kilos, un total de: " + str(dic.get(v_fruta) * v_kilos))
else:
    print("Fruta no en lista")








