# Haz que el usuario introduzca números enteros por teclado. Mientras el usuario no introduzca el 0, muestra
# si el número introducido es par o impar

v_num_in = int(input('Ingrese número entero: '))

while v_num_in != 0:

    if v_num_in % 2 == 0:
        print('Es par')
        v_num_in = int(input('Ingrese número entero: '))

    else:
        print('Es impar')
        v_num_in = int(input('Ingrese número entero: '))


print('Ingresaste el valor prohibido, chau!!!')


