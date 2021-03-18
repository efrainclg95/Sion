'''Escribir una función que reciba una diccionario con las notas de los alumnos en curso en un examen y
devuelva una serie con las notas de los alumnos aprobados ordenadas de mayor a menor.'''

import pandas as pd

def notas_alumnos(diccionario):

    s = pd.Series(diccionario)
    s = s.sort_values()

    return s

print(notas_alumnos({'efrain':12,'felipe':20,'karina':19,'guido':5}))