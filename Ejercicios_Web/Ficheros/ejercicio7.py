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

minimo = {}
maximo = {}
media = {}

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

            # print(list_t) # lista con valores enteros, no existe str

            for a, b in enumerate(list_t):

                print(a, b)


    return

# print(operation_clean(fopen()))
print(structured(operation_clean(fopen())))
# print(operations(structured(operation_clean(fopen()))))

