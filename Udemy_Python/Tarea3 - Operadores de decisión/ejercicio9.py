# Haz un usuario introduza una letra y comprueba si se trata de una vocal. Si el usuario introduce un string
# de más de un carácter, infórmale de que no se puede procesar el dato, pues debe tener como máximo tamaño
# 1.
# PISTA: Convierte la letra introducida a minúsculas para tener que realizar menos comprobaciones

v_letra = str(input('Introduzca una letra: '))

v_vocales = 'a', 'e', 'i', 'o', 'u'

if len(v_letra) == 1:
    print('Correcto, tiene un caracter')
    if v_letra in v_vocales:
        print('es una vocal')
    else:
        print('{} no es una vocal'.format(v_letra))
else:
    print('Tiene mas de un caracter')


