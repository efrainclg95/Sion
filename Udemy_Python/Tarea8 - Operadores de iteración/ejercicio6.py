# Haz que el usuario introduzca dos números enteros por teclado. El primero será el extremo izquierdo del
# intervalo y, el segundo, el extremo derecho. Imprime todos los números que se encuentren entre los dos
# números introducidos por el usuario (los extremos incluidos).

v_num_inicio = int(input('Ingrese primer número: '))
v_num_fin = int(input('Ingrese ultimo número: '))

for num in range(v_num_inicio,v_num_fin + 1):
    print(num)
