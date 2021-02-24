from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://news.google.com/covid19/map?hl=es-419&gl=PE&ceid=PE%3Aes-419'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

pais = soup.find_all('div', class_= 'pcAJd')

print(pais)





