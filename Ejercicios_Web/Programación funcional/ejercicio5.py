"""Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud."""

frase = 'Felipe bello bebe'

def f_out_dic(frase):
    lista_frase = []
    for i in frase:
        lista_frase = frase.split()
    return lista_frase

def f_longitud_frase(lista):
    dic = {}
    for j,k in enumerate(f_out_dic(frase)):
        dic[f_out_dic(frase)[j]] = len(k)
    return dic

#print(f_out_dic(frase))
print(f_longitud_frase(f_out_dic(frase)))

