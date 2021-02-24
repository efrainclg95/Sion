from bs4 import BeautifulSoup
import requests
import pandas as pd

paises = []
casos_hoy = []
total_casos = []

url = 'https://news.google.com/covid19/map?hl=es-419&gl=PE&ceid=PE%3Aes-419'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

pais = soup.find_all('div', class_= 'pcAJd')
cantidad = soup.find_all('td', class_= 'l3HOY')


for p in pais:
    paises.append(p.text)

contador = 0

while contador <= 1000:
    contador = contador + 5
    # print(contador)

    for j, k in enumerate(cantidad):

        if j == contador:
            total_casos.append(k.text)

print(total_casos)

        # print(j,k)










