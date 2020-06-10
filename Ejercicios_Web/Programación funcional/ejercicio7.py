"""Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y
las calificaciones correspondientes a las notas."""

# Sol 1

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

def dic_califica(dic):
    out_dic = {}
    for keys,values in dic.items():
        out_dic[keys.upper()] = califica(values)
        # print(keys,values)
    return out_dic

dic = {'matemáticas': 10, 'lenguaje' : 3.5}

print(dic_califica(dic))




