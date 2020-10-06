"""Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>."""


# Sol 1

'''def save_dic(nombre,edad,direccion,telefono):
    dic = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
    for keys,values in dic.items():
        dic[keys] = values
        # print(str(dic.get('nombre')) + ' tiene' + str(dic.get('edad')) + ' vive en ' + str(dic.get('direccion')) + ' y su número telefonico es: ' + str(dic.get('telefono')))
    # return dic
    return dic,(str(dic.get('nombre')) + ' tiene ' + str(dic.get('edad')) + ' años, vive en ' + str(dic.get('direccion')) + ' y su número telefonico es: ' + str(dic.get('telefono')))

print(save_dic('efrain',35,'betania',963752034))'''

# Sol 2

def save_dic(nombre,edad,direccion,telefono):
    lista_datos = ['nombre','edad','direccion','telefono']
    lista_input = [nombre,edad,direccion,telefono]
    dic = dict(zip(lista_datos,lista_input))
    # return dic
    return (str(dic.get('nombre')) + ' tiene ' + str(dic.get('edad')) + ' años, vive en ' + str(dic.get('direccion')) + ' y su número telefonico es: ' + str(dic.get('telefono')))

print(save_dic('efrain',35,'betania',963752034))