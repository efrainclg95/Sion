'''El fichero calificaciones.csv contiene las calificaciones de un curso. Durante el curso se realizaron dos exámenes parciales de teoría y un examen de prácticas.
Los alumnos que tuvieron menos de 4 en alguno de estos exámenes pudieron repetirlo en la al final del curso (convocatoria ordinaria).

Escribir un programa que contenga las siguientes funciones:

Una función que reciba el fichero de calificaciones y devuelva una lista de diccionarios, donde cada diccionario contiene la información de los exámenes y la asistencia de un alumno. La lista tiene que estar ordenada por apellidos.

Una función que reciba una lista de diccionarios como la que devuelve la función anterior y añada a cada diccionario un nuevo par con la nota final del curso.
El peso de cada parcial de teoría en la nota final es de un 30% mientras que el peso del examen de prácticas es de un 40%.

Una función que reciba una lista de diccionarios como la que devuelve la función anterior y devuelva dos listas, una con los alumnos aprobados y otra con los alumnos suspensos.
Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes parciales y de prácticas mayor o igual que 4 y la nota final mayor o igual que 5.'''

registro = str('calificaciones_limpio.csv')
lista_f1 = []

def tratamiento(lista1):

    lista2 = []

    for j in lista1:

        if j == '': # convierte los espacios vacios en 0
            j = 0

        v_str_j = str(j)
        v_len_j = len(v_str_j)

        if v_len_j >= 1:
            v_ntrat = v_str_j[0] + '.' + v_str_j[1:9]
            lista2.append(float(v_ntrat)) # tipo de dato de los valores numéricos de la lista

    return lista2

def conversion_porcentaje(lista_valor):

    v_int = int(float(lista_valor) * 100)

    return (str(v_int) + '%')

def lista_final1(lista_mayor):

    lista_mayor = max(lista_mayor[3],lista_mayor[5]) # calcula el valor mayor de dos valores indice 3 y 5 de la lista general

    return lista_mayor

def lista_final2(lista_mayor):

    lista_mayor = max(lista_mayor[4],lista_mayor[6]) # calcula el valor mayor de dos valores indice 4 y 6 de la lista general

    return lista_mayor

def lista_finalprac(lista_mayor):

    lista_mayor = max(lista_mayor[7],lista_mayor[8]) # calcula el valor mayor de dos valores indice 7 y 8 de la lista general

    return lista_mayor

def nota_fin(lista_nfin):

    lista_nfin = lista_nfin[9] * 0.3 + lista_nfin[10] * 0.3 + lista_nfin[11] * 0.4 # calcula la notal final

    return lista_nfin

def lista_dic(registro):

    f = open(registro,'r')
    f = f.readlines()

    # Proceso de limpieza

    for j,k in enumerate(f):
        k = k.strip()  # elimina espacios, salto de línea y tabulaciones
        k = k.replace('\xad','') # limpia el caracter \xad (-)

        k = k.split(',') # lista todos los registros con orden correspondiente "h"
        # print(j,k)

        if j == 0:
            lista_key = k # lista para keys
            lista_key.append('Final1')
            lista_key.append('Final2')
            lista_key.append('FinalPracticas ')
            lista_key.append('NotaFinal')
            # print(lista_key)

        elif j >= 1:
            lista_values = k # lista para valores
            # print(lista_values)

            lista_values[3:9] = tratamiento(lista_values[3:9]) # reemplaza los valores de la lista[3:9] por los valores tratados en tratamiento(lista_values[3:9]

            lista_values[2] = conversion_porcentaje(lista_values[2]) # reemplaza los valores de la lista[2] por un valor en cadena agregando el %

            lista_values.append(lista_final1(lista_values)) # se agrega a la lista el valor mayor de la comparación que ejecuta la función lista_final1

            lista_values.append(lista_final2(lista_values))  # se agrega a la lista el valor mayor de la comparación que ejecuta la función lista_final2

            lista_values.append(lista_finalprac(lista_values))  # se agrega a la lista el valor mayor de la comparación que ejecuta la función lista_finalprac

            lista_values.append(nota_fin(lista_values)) # se agrega la nota final luego de procesar la función nota_fin

            # print(lista_values)

            dic_f1 = dict(zip(lista_key,lista_values)) # se combina lista_key con lista_values para obtener diccionarios
            lista_f1.append(dic_f1) # se obtiene lista con diccionarios

    return (lista_f1)

print(lista_dic(registro))


# print(conversion_porcentaje(0.35 ))
# print(lista_max([4,5,6,5,2,4,8,9,3]))

