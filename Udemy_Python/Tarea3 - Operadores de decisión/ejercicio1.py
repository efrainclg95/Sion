# Haz que un usuario introduzca un número real y evalúa si dicho número es positivo, negativo o cero. Devuelve
# por pantalla el resultado en cada caso.

v_num = int(input('Ingrese un número: '))
if v_num > 0:
    print('{} Es un número positivo'.format(v_num))
elif v_num == 0:
    print('{} Es cero'.format(v_num))
elif v_num < 0:
    print('{} Es un número negativo'.format(v_num))

