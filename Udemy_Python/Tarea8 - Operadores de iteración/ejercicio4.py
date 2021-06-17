# Haz que el usuario introduzca números enteros por teclado. Mientras el usuario no introduzca el 0, calcula
# cuántos números positivos y cuántos negativos ha introducido y muéstraselo al final.


v_num = int(input('Ingrese número: '))
contador_p = 0
contador_n = 0

while v_num != 0:
    if v_num > 0:
        contador_p += 1
    elif v_num < 0:
        contador_n += 1
    v_num = int(input('Ingrese número: '))

else:
    print('Fin de proceso')
    print('Números positicos {} y números negativos {}'.format(contador_p,contador_n))


