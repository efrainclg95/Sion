"""Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso
{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura
en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y
<créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso."""

def funcion(diccionario):
    total_creditos = 0
    for keys,values in diccionario.items():
        total_creditos += diccionario.get(keys)
        cadena = str(keys) + ' tiene ' + str(values) + ' créditos'
        print(cadena)
    return str(total_creditos) + ' créditos totales'

print(funcion({'Matemáticas': 6, 'Física': 4, 'Química': 5}))
