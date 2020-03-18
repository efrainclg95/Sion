# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y
# la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

print("Defina cuantos cursos puede llevar")

v_cantidad_cursos = int(input("Ingrese del 1 al 7 el número de cursos que desea llevar: "))
v_lista_cursos = []

if v_cantidad_cursos <= 7:

    for i in range(1,v_cantidad_cursos + 1):
        v_cursos = str(input("Registre el curso {}".format(i) + ": "))
        v_lista_cursos.append(v_cursos)
    print("Usted llevará los cursos siguientes: {}".format(v_lista_cursos).upper())

else:
    print("No puede llevar mas de 7 cursos")
