# Escribir un programa que muestre el eco de
# todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

# Sol 1

v_input = str(input("Introduce algo: ").upper())

while v_input != "":
    v_input = str(input("Introduce algo: ").upper())
    if v_input == "SALIR":
        print("FIN")
        break




