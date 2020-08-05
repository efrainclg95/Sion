"""Escribir un programa que abra el fichero con información sobre el PIB per cápita de los países de la Unión Europea
(url:https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true),
pregunte por las iniciales de un país y muestre el PIB per cápita de ese país de todos los años disponibles"""

# Sol 1

def open_www(www):
    from urllib import request
    f = request.urlopen(www)
    contenido = f.read()
    # print(contenido.decode('utf-8'))

    lista0 = contenido.decode('utf-8').split('\n')
    # print(lista0)

    for i in lista0:
        lista1 = i.split('\t')
        cadena0 = lista1[0]
        lista2 = cadena0.split(',')
        print(lista2[2])

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
        result = {data['years'][i]: data[country][i] for i in range(len(data['years']))}

        return result

country = input('Introduce el código de un país: ')
print('Producto Interior Bruto per cápita de', country)
print('Año', '\t', 'PIB')
for year, pib in open_f('https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?file=data/sdg_08_10.tsv.gz&unzip=true').items():
    print(year, '\t', pib)'''
