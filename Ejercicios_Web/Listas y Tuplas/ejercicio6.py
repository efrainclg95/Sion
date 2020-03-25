# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
# pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

# Sol1

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
nota_asignatura = []

for i in range(len(asignaturas)):
    v_nota = int(input("Ingrese nota de " + asignaturas[i] + ": "))
    nota_asignatura.append(v_nota)

for j in range(len(nota_asignatura)):
    if nota_asignatura[j] <= 10:
        nota_asignatura.append(j)
        print("Asignaturas desaprobadas: " + str(asignaturas[j]) + " con nota de: " + str(nota_asignatura[j]))





