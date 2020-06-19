"""Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>."""


def save_dic(nombre,edad):
    dic = {nombre}
    dic[nombre] = nombre
    return dic

print(save_dic('efrain',35))
