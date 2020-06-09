"""Escribir una función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas."""

''''# Sol 1

def califica(n):

    if n < 5:
        return 'SS'
    elif n < 7:
        return 'AP'
    elif n < 9:
        return 'NT'
    elif n < 10:
        return 'SB'
    else:
        return 'MH'

def notas(lista):

    lista_califica = []

    for i in lista:
        lista_califica.append(califica(i))
    return lista_califica

print(notas([4,5,3.2,9,10]))'''

# Sol 2

def califica(n):

    if n < 5:
        return 'SS'
    elif n < 7:
        return 'AP'
    elif n < 9:
        return 'NT'
    elif n < 10:
        return 'SB'
    else:
        return 'MH'

def notas(lista):
    return list(map(califica,lista))

print(notas([4,5,3.2,9,10]))