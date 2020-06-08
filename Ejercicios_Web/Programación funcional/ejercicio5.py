"""Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud."""

frase = 'Felipe bello bebe'
lista_frase = []

def f_out_dic(frase):
    for i in frase:
        lista_frase = frase.split()
    return lista_frase

print(f_out_dic(frase))

