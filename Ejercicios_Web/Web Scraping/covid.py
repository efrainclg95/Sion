from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://news.google.com/covid19/map?hl=es-419&gl=PE&ceid=PE%3Aes-419'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

pais = soup.find_all('div', class_= 'pcAJd')
cantidad = soup.find_all('td', class_= 'l3HOY')

paises = []
total_casos = []

for p in pais:
    paises.append(p.text)


for j,k in enumerate(cantidad):
    contador = -5
    while contador < 300 :
        contador = contador + 5
        # print(j)
        if j == contador:
            # print(j,k.text)
            total_casos.append(k.text)

# Solución en base a diccionarios

'''dic_covid = dict(zip(paises,total_casos))

v_in_pais = input(str('Ingrese país a consultar: '))
v_out_resultado = str('La cantidad actual de casos COVID19 en '+ v_in_pais + ' es de: ' + dic_covid.get(v_in_pais))

print(v_out_resultado)'''

# Solución usando Pandas

df = pd.DataFrame({'Pais': paises,'Total de Casos': total_casos})
print(df)



'''df = pd.DataFrame({'Nombre':equipos,'Puntos':puntos}, index = list(range(1,21)))

print(df)'''














