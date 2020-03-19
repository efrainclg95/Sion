# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
# pregunte al usuario la nota que ha sacado en cada asignatura,
# y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y
# <nota> cada una de las correspondientes notas introducidas por el usuario.

lista_asignatura = []
lista_nota_asignatura = []

for asignatura in range(1,3 + 1):
    v_ingresa_asignatura = str(input("Ingrese Asignatura {}".format(asignatura) + ": "))
    lista_asignatura.append(v_ingresa_asignatura)
print("Asignaturas Registradas: " + str(lista_asignatura))

for nota_asignatura in lista_asignatura:
    v_ingresa_nota = int(input("Ingrese Nota de la Asignatura {}".format(nota_asignatura) + ": "))
    lista_nota_asignatura.append(v_ingresa_nota)
print("Notas Ingresadas: " + str(lista_nota_asignatura))

for i in range(len(lista_asignatura)):
    print("Su nota en " + str(lista_asignatura[i]) + " es de: " + str(lista_nota_asignatura[i])  )








