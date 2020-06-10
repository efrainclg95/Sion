"""Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y
las calificaciones correspondientes a las notas."""

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

print(califica(10))