from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://news.google.com/covid19/map?hl=es-419&gl=PE&ceid=PE%3Aes-419'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

pais = soup.find_all('div', class_= 'pcAJd')
cantidad = soup.find_all('td', class_= 'l3HOY')

paises = []
infectados_hoy = []

for p in pais:
    paises.append(p.text)

for i in cantidad:
    infectados_hoy.append(i.text)

# print(paises)
print(infectados_hoy)







