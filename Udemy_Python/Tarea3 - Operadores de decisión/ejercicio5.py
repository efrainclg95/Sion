# Haz que un usuario introduzca dos números enteros positivos. Suponiendo que el primer número introducido
# por el usuario es mayor o igual al segundo número introducido por el usuario, comprueba que la división del
# primer número entre el segundo número es entera.
# En caso de la división ser entera, devuelve el cociente por pantalla e indica que la división en efecto es entera.
# En caso de la división no ser entera, devuelve el cociente y el resto por pantalla e indica que la división entre
# los dos números no es entera.


x = int(input('Ingrese el valor de X: '))
y = int(input('Ingrese el valor de Y: '))

if x >= y:

    cociente = x // y
    residuo = x % y

    if residuo >= 0 and residuo < y:
        print('Es una div entera, su cociente es: {}'.format(cociente))

    else:
        print('La div no es entera, su cociente es: {} y su residuo es: {}'.format(cociente,residuo))

else:
    print('x no es mayor o igual a y')
