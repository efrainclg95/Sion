# Haz que el usuario introduzca dos números enteros por teclado. El primero será el extremo izquierdo del
# intervalo y, el segundo, el extremo derecho. Imprime la suma de todos los múltiplos de 3 que se encuentren
# entre los dos números introducidos por el usuario (los extremos incluidos). Finalmente, muestra por pantalla
# el resultado de la suma.

v_num_inicio = int(input('Ingrese primer número: '))
v_num_fin = int(input('Ingrese ultimo número: '))

for num in range(v_num_inicio,v_num_fin + 1):

    if num % 3 == 0:
        v_sum_m3 = num + num

print('La suma de los múltiplos de 3 es: {}'.format(v_sum_m3))


