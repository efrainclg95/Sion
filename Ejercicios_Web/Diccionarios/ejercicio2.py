# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

v_nombre = str(input("Ingrese su nombre: "))
v_edad = int(input("Ingrese su edad: "))
v_direccion = str(input("Ingrese su dirección: "))
v_telefono = int(input("Ingrese su número telefónico: "))

dic = {'nombre' : v_nombre, 'edad' : v_edad, 'direccion' : v_direccion, 'telefono' : v_telefono}

print(dic.get('nombre') + " tiene " + str(dic.get('edad')) + " años, vive en: " + dic.get('direccion') + " y su número telefónico es: " + str(dic.get('telefono')))


