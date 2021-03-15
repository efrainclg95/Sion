'''Escribir una función que reciba una diccionario con las notas de los alumnos en curso en un examen y
devuelva una serie con la nota mínima, la máxima, media y la desviación típica.'''

import pandas as pd

# Solución 1

'''def serie_notas(diccionario):

    s = pd.Series(diccionario)
    s = pd.Series([s.max(),s.min(),s.mean(),s.std()], index=['max','min','mean','std'])

    return s

print(serie_notas({'Juan':9, 'María':6.5, 'Pedro':4, 'Carmen': 8.5, 'Luis': 5}))'''

# Soluciòn 2

def serie_notas(diccionario):

    s = pd.Series(diccionario)
    s = s.describe()

    return s

print(serie_notas({'Juan': 9, 'María': 6.5, 'Pedro': 4, 'Carmen': 8.5, 'Luis': 5}))


