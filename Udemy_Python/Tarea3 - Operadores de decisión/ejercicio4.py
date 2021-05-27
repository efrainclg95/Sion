# Haz que un usuario introduzca dos números enteros positivos. Comprueba si el primer número introducido
# por el usuario es mayor o igual que el segundo número introducido por el usuario. Devuelve por pantalla el
# resultado en cada caso.

v_x = int(input('Ingrese el valor de X: '))
v_y = int(input('Ingrese el valor de Y: '))

print('{} es mayor que {}'.format(v_x,v_y)) if v_x > v_y else print('{} es menor que {}'.format(v_x,v_y))