"""Escribir un programa que abra el fichero con información sobre el PIB per cápita de los países de la Unión Europea
(url:https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true),
pregunte por las iniciales de un país y muestre el PIB per cápita de ese país de todos los años disponibles"""

# Sol 1

def open_www(www):
    from urllib import request
    f = request.urlopen(www)
    contenido = f.read()

    lista0 = contenido.decode('utf-8')
    lista0 = lista0.split('\n')

    for j,k in enumerate(lista0):
        # lista0 = list(k.split())
        lista0 = list(k.split('\t'))

        if j == 0:
            lista0.pop(0)
            lista_tiempo = lista0
            # print(lista_tiempo) # Lista de Tiempo = lista_tiempo
        else:
            j > 0
            lista1 = list(k.split('\t'))
            lista_pais = lista1
            print(lista_pais)






print(open_www('https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true'))


# Sol 2

'''def open_f(url):
    from urllib import request
    from urllib.error import URLError

    try:
        file = request.urlopen(url)
    except URLError:
        print('No existe URL dada')
    else:
        data = file.read().decode('utf-8').split('\n')
        data = [i.split('\t') for i in data]
        data = [list(map(str.strip, i)) for i in data]

        for i in data:
            i[0] = i[0].split(',')[-1]

        data[0][0] = 'years'

        data = {i[0]: i[1:] for i in data}
        
        print(data)

        result = {data['years'][i]: data[country][i] for i in range(len(data['years']))}

        return result

country = input('Introduce el código de un país: ')
print('Producto Interior Bruto per cápita de', country)
print('Año', '\t', 'PIB')
for year, pib in open_f('https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true').items():
    print(year, '\t', pib)

print(open_f('https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true'))'''
