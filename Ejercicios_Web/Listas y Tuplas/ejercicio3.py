# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
# pregunte al usuario la nota que ha sacado en cada asignatura,
# y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y
# <nota> cada una de las correspondientes notas introducidas por el usuario.

# Sol 1

v_lista_asignatura = []
v_nota_asignatura = []

for asignatura in range(1,4):
    v_asignatura = str(input("Ingrese asignatura {}".format(asignatura) + ": "))
    v_lista_asignatura.append(v_asignatura)

print("Asignaturas registradas: " + str(v_lista_asignatura))

for nota in v_lista_asignatura:
    v_nota = int(input("Ingrese nota de " + nota + ": "))
    v_nota_asignatura.append(v_nota)

print("Notas registradas: " + str(v_nota_asignatura))

for i in range(len(v_lista_asignatura)):
    print("En " + str(v_lista_asignatura[i]) + " sacaste: " + str(v_nota_asignatura[i]))







