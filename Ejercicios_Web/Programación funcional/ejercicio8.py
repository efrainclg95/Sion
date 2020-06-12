"""Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno
y devuelva otro diccionario con las asignaturas en mayúsculas
y las calificaciones correspondientes a las notas aprobadas."""

# Sol 1

""""

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


def dic_califica(scores):
    dic_aprobados = {}
    for keys,values in scores.items():
        if values >= 5:
            dic_aprobados[keys.upper()] = califica(values)
    return dic_aprobados

print(dic_califica({'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':8.2, 'Historia':9.7, 'Programación':10}))"""

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

def nota_aprobada(nota):
    return (nota[1] >= 5) # duda con esta función

def dic_califica(dic_notas):

    proceso = dict(filter(nota_aprobada, dic_notas.items()))
    asignatura = map(str.upper,proceso.keys())
    puntaje = map(califica,proceso.values())

    return dict(zip(asignatura,puntaje))

print(dic_califica({'Matemáticas': 6.5, 'Física': 5, 'Química': 3.4, 'Economía': 8.2, 'Historia': 9.7, 'Programación': 10}))

