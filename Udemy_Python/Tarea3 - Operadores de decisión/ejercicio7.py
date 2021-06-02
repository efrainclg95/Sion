# Haz que un usuario introduzca dos números enteros positivos. Comprueba si el mayor es múltiplo del menor.
# Devuelve por pantalla el resultado en cada caso

v_num1 = int(input('Ingrese primer número: '))
v_num2 = int(input('Ingrese segundo número: '))

if v_num1 > v_num2:
    print(str(v_num1), 'es mayor a:',str(v_num2))
    operacion = v_num1 % v_num2

    if operacion == 0:
        print('{} es múltiplo de: {}'.format(v_num1,v_num2))
    else:
        print('{} no es múltiplo de: {}'.format(v_num1, v_num2))

else:
    print(str(v_num2), 'es mayor a:',str(v_num1))
    operacion = v_num2 % v_num1

    if operacion == 0:
        print('{} es múltiplo de: {}'.format(v_num2,v_num1))
    else:
        print('{} no es múltiplo de: {}'.format(v_num2, v_num1))