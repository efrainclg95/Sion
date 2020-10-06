"""Escribir un programa que cree un diccionario vacío y lo vaya llenando con información sobre una persona
(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario."""

dato = str(input('Que dato quiere ingresar: '))

def dato_persona(dato):
    dic = {}
    dic[dato] = input(dato + ': ')
    continua = str(input('Quieres añadir más información (Si/No): '))

    while continua == 'Si':
        dato = str(input('Que dato quiere ingresar: '))
        dic[dato] = input(dato + ': ')
        continua = str(input('Quieres añadir más información (Si/No): '))

    return dic

print(dato_persona(dato))

