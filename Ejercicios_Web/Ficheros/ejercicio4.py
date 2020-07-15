"""Escribir un programa que acceda a un fichero de internet mediante su url
y muestre por pantalla el número de palabras que contiene."""

# Sol1

'''from urllib import request

def lectura_url(www):
    f = request.urlopen(www)
    datos = f.read()
    return datos.decode('utf-8')

def num_palabras(finter):
    contador_lista = finter.split()
    # print(contador_lista)
    return len(contador_lista)

# print(lectura_url('https://raw.githubusercontent.com/asalber/asalber.github.io/master/README.md'))
print(num_palabras(lectura_url('https://www.gutenberg.org/cache/epub/2000/pg2000.txt')))'''

# Sol2

def words_file(url):
    '''
    Función que recibe recibe la url de un fichero de texto y devuelve el número de palabras que contiene.
    Parámetros:
        url: Es una cadena con la url del fichero de texto.
    Devuelve:
        El número de palabras que contiene el fichero de texto daro por la url.
    '''
    from urllib import request
    from urllib.error import URLError
    try:
        file = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        content = file.read()
        return len(content.split())

print(words_file('https://www.gutenberg.org/cache/epub/2000/pg2000.txt'))
print(words_file('https://no-existe.txt'))

