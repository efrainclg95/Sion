'''El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35
con las siguientes columnas: nombre (nombre de la empresa),
Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada),
Mínimo (precio mínimo de la acción durante la jornada), volumen (Volumen al cierre de bolsa),
Efectivo (capitalización al cierre en miles de euros).
Construir una función que construya un DataFrame a partir del un fichero con el formato anterior y
devuelva otro DataFrame con el mínimo, el máximo y la media de dada columna.'''

import pandas as pd

# Sol1

'''datos_fichero = pd.read_csv('cotizacion.csv', sep=';', thousands='.', decimal=',', index_col=0)

datos_fichero = pd.DataFrame([datos_fichero.max(),datos_fichero.min(),datos_fichero.mean()], index=['max','min','media'])

print(datos_fichero)'''

# Sol2

def construye_df(fichero):

    fichero = pd.DataFrame([fichero.max(), fichero.min(), fichero.mean()],index=['max', 'min', 'media'])

    return fichero

print(construye_df(pd.read_csv('cotizacion.csv', sep=';', thousands='.', decimal=',', index_col=0)))







