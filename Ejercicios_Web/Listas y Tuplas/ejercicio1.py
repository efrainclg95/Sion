# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista y la muestre por pantalla.

print ("Ingrese 5 Asignaturas")
v_lista = []

for i in range(1,6):
    v_asignatura = input("Ingrese asignatura " + str(i) + ": ")
    v_lista.append(v_asignatura)

print(v_lista)
#print(v_lista[0])

