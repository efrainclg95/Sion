# Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso
# {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura
# en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y
# <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

dic_asignatura = {'Matemáticas' : 6 , 'Física' : 4, 'Química' : 5}
sum = 0

for i in dic_asignatura:
    sum = sum + dic_asignatura.get(i)
    print(i + " tiene " + str(dic_asignatura.get(i)) + " créditos")

print("Número total de créditos del curso: {}".format(sum))

