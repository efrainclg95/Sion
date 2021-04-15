'''El fichero titanic.csv contiene información sobre los pasajeros del Titanic. Escribir un programa con los siguientes requisitos:

Generar un DataFrame con los datos del fichero.
Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas
Mostrar por pantalla los datos del pasajero con identificador 148.
Mostrar por pantalla las filas pares del DataFrame.
Mostrar por pantalla los nombres de las personas que iban en primera clase ordenadas alfabéticamente.
Mostrar por pantalla el porcentaje de personas que sobrevivieron y murieron.
Mostrar por pantalla el porcentaje de personas que sobrevivieron en cada clase.
Eliminar del DataFrame los pasajeros con edad desconocida.
Mostrar por pantalla la edad media de las mujeres que viajaban en cada clase.
Añadir una nueva columna booleana para ver si el pasajero era menor de edad o no.
Mostrar por pantalla el porcentaje de menores y mayores de edad que sobrevivieron en cada clase.'''


import pandas as pd

# Generar un DataFrame con los datos del fichero.
# titanic = pd.read_csv('titanic.csv', index_col=0)
titanic = pd.read_csv('titanic.csv')

'''print(titanic)

# Mostrar por pantalla las dimensiones del DataFrame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas

print('Dimensiones: ', titanic.shape)
print('Nùmero de Datos: ', titanic.size)
print('Nombres de Columnas: ', titanic.columns)
print('Nombres de Filas: ', titanic.index)
print('Tpos de Datos de Columnas: ', titanic.dtypes)
print('10 Primeras Filas: ', titanic.head(10))
print('10 Ultimas Columnas: ', titanic.tail(10))

# Mostrar por pantalla los datos del pasajero con identificador 148

print('Pasajero Id 148: ', titanic.loc[148])'''

# Mostrar por pantalla las filas pares del DataFrame

v_cfilas = titanic.shape[0] # cantidad de filas (891)










