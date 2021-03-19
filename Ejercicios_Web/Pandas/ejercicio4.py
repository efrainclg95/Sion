'''Escribir programa que genere y muestre por pantalla un DataFrame con los datos de la tabla siguiente:'''

import pandas as pd

datos = {'Mes':['Enero','Febrero','Marzo','Abril'],'Ventas':[30500,35600,28300,33900],'Gastos':[22000,23400,18100,20700]}
df = pd.DataFrame(datos)

print(df)