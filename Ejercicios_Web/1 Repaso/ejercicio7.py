# Escribir un programa que muestre el eco de
# todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

v_palabra = str('frase')

while v_palabra != '':
    v_palabra = str(input("Ingrese palabra: "))
    print(v_palabra)
    if v_palabra == 'salir':
        print("eso es todo")
        break

