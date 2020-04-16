# Escribir un programa que cree un diccionario vacío y lo vaya llenando con información sobre una persona
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
# que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

dic = {}

v_dato = str(input("Que dato quieres introducir: ").upper())
v_d1 = str(input(v_dato + ": ")).upper()

dic[v_dato] = v_d1

print(dic)

consulta = str(input("Quieres añadir más información (Si/No): ").upper())

while consulta == 'SI':
    v_dato = str(input("Que dato quieres introducir: ").upper())
    v_d1 = str(input(v_dato + ": ")).upper()
    dic[v_dato] = v_d1
    print(dic)
    consulta = str(input("Quieres añadir más información (Si/No): ").upper())

print("FIN")










