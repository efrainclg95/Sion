# Haz que el usuario introduzca una palabra y una letra por teclado. Comprueba si la palabra contiene la
# letra o no e indícaselo al usuario por pantalla.

v_palabra = str(input('Ingrese una palabra: ').lower())
v_letra = str(input('Ingrese una letra: ').lower())

for letras in v_palabra:

    if v_letra == letras:
        print('La letra ingresada forma parte de la palabra')
        break
    else:
        print('La letra ingresada NO forma parte de la palabra')
        break



