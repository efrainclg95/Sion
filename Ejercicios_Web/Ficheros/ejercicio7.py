'''El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas:

Nombre (nombre de la empresa),
Final (precio de la acción al cierre de bolsa),
Máximo (precio máximo de la acción durante la jornada),
Mínimo (precio mínimo de la acción durante la jornada),
Volumen (Volumen al cierre de bolsa),
Efectivo (capitalización al cierre en miles de euros).

Construir una función reciba el fichero de cotizaciones y devuelva un diccionario con los datos del fichero por columnas.

Construir una función que reciba el diccionario devuelto por la función anterior y
cree un fichero en formato csv con el mínimo, el máximo y la media de dada columna.'''

lista_final = []
lista_max = []
lista_min = []
lista_vol = []
lista_efectivo = []

dic_min = {}
dic_max = {}
dic_media = {}

import statistics as stats

def fopen():

    f = open('cotizacion.csv','r')
    general_list = f.readlines()
    return general_list

def clean(valor): # elimina la ','

    valor = valor.replace(',','')
    return valor

def operation_clean(lista_general):

    list_c = []

    for i in lista_general:
        i = clean(i)
        i = i.strip() # elimina espacios, salto de línea y tabulaciones

        list_c.append(i)

    return list_c # lista limpia

def structured(lista_limpia):

    for j, k in enumerate(lista_limpia):
        list_s = k.split(';')

        if j  > 0: # se elimina la cabecera principal
            # print(list_s) # imprime listas sin cabeceras

            list_s.pop(0) # elimina elemento 0 de lista
            # print(list_s)

            list_t = []
            for j, k in enumerate(list_s):
                if j <= 2 or j == 4:
                    list_t.append(int(k))
                else:
                    list_t.append(int(k.replace('.',''))) # reemplaza el . por ''

            for a, b in enumerate(list_t):
                # print(a, b)
                if a == 0:
                    lista_final.append(b) # lista campo final
                elif a == 1:
                    lista_max.append(b)  # lista campo maximo
                elif a == 2:
                    lista_min.append(b)  # lista campo minimo
                elif a == 3:
                    lista_vol.append(b)  # lista campo volumen
                elif a == 4:
                    lista_efectivo.append(b)  # lista campo efectivo

    # print(lista_final)
    # print(lista_max)
    # print(lista_min)
    # print(lista_vol)
    # print(lista_efectivo)

    dic_min = {'Nombre': 'Mínimo', 'Final': min(lista_final), 'Máximo': min(lista_max), 'Mínimo': min(lista_min), 'Volumen': min(lista_vol), 'Efectivo': min(lista_efectivo)}
    dic_max = {'Nombre': 'Máximo', 'Final': max(lista_final), 'Máximo': max(lista_max), 'Mínimo': max(lista_min), 'Volumen': max(lista_vol), 'Efectivo': max(lista_efectivo)}
    dic_media = {'Nombre': 'Media', 'Final': stats.mean(lista_final), 'Máximo': stats.mean(lista_max), 'Mínimo': stats.mean(lista_min), 'Volumen': stats.mean(lista_vol), 'Efectivo': stats.mean(lista_efectivo)}

    # print(dic_min)
    # print(dic_max)
    # print(dic_media)

    # f = open('informe_cotizacion.csv','w')

    l_str1 = []
    l_str2 = []
    l_str3 = []
    l_str4 = []

    for keys, values in dic_min.items():
        l_str1.append(keys)
        str1 = ";".join(l_str1) # convierte lista a cadena poniendo un ";" como separador
    print(str1)


    for keys, values in dic_min.items():
        # print(keys, values)
        l_str2.append(str(values))
        str2 = ";".join(l_str2)  # convierte lista a cadena poniendo un ";" como separador
    print(str2)

    for keys, values in dic_max.items():
        # print(keys, values)
        l_str3.append(str(values))
        str3 = ";".join(l_str3)  # convierte lista a cadena poniendo un ";" como separador
    print(str3)

    for keys, values in dic_media.items():
        # print(keys, values)
        l_str4.append(str(values))
        str4 = ";".join(l_str4)  # convierte lista a cadena poniendo un ";" como separador
    print(str4)



print(structured(operation_clean(fopen())))

# print(armed(lista_final))

