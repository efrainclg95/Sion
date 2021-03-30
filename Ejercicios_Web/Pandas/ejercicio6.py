'''El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35
con las siguientes columnas: nombre (nombre de la empresa),
Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada),
Mínimo (precio mínimo de la acción durante la jornada), volumen (Volumen al cierre de bolsa),
Efectivo (capitalización al cierre en miles de euros).
Construir una función que construya un DataFrame a partir del un fichero con el formato anterior y
devuelva otro DataFrame con el mínimo, el máximo y la media de dada columna.'''

import pandas as pd

datos_fichero = pd.read_csv('cotizacion.csv', sep=';', decimal=',')

# datos_fichero = datos_fichero.index([datos_fichero.max(),datos_fichero.min(),datos_fichero.mean(),datos_fichero.std()], index=['max','min','mean','std'])

datos_fichero = pd.DataFrame([datos_fichero.max(),datos_fichero.min(),datos_fichero.mean()], index=['max','min','media'])

print(datos_fichero)



