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


def fopen():

    f = open('cotizacion.csv','r')
    general_list = f.readlines()
    return general_list

def clean(valor):

    valor = valor.replace(',','')
    # return float(valor)
    return valor

def operation_clean(lista_geneal):

    # print(lista_geneal)

    for i in lista_geneal:
        i = clean(i)
        print(i)



print(operation_clean(fopen()))



'''for i in file_list:  # nuevo
    str_list.append(i.rstrip('\n'))  # función elimina \n'''