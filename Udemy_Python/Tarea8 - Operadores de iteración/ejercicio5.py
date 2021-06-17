# Haz que el usuario introduzca números por teclado. Mientras el usuario no introduzca el 0, pídele otro
# número. Cuando el usuario introduzca el 0, muéstrale la media aritmética de los números que ha introducido.

v_num = ''
v_sum = 0
v_itera = 0

while v_num != 0:

    v_num = int(input('Ingrese número: '))
    v_sum = v_sum + v_num
    v_itera += 1

else:
    print('Su media aritmética es: {}'.format(v_sum/v_itera))




