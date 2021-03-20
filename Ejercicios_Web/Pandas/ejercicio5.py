'''Escribir una función que reciba un DataFrame con el formato del ejercicio anterior,
una lista de meses, y devuelva el balance (ventas - gastos) total en los meses indicados.'''

import pandas as pd

def df_datos(diccionario):

    df = pd.DataFrame(diccionario)
    bal = df.Ventas - df.Gastos
    df['Balance'] = pd.Series(bal)

    # return df.loc[2, 'Gastos']
    return df

print (df_datos({'Mes':['Enero','Febrero','Marzo','Abril'],'Ventas':[30500,35600,28300,33900],'Gastos':[22000,23400,18100,20700]}))


