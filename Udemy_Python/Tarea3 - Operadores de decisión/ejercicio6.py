# Fusiona lo hecho en los ejercicios 4 y 5 para que
# 1. Un usuario introduzca dos números enteros por pantalla.
# 2. Comprobar si el primer número es mayor o igual al segundo número introducido por el usuario. Devolver
# por pantalla en que caso nos encontramos.
# 3. Hacer la división entera pertinente en cada caso.
# 4. Si la división es entera, entonces devolver por pantalla el cociente e indicar que la división es entera.
# Si la división no es entera, entonces devolver por pantalla el cociente y el resto e indicar que la división realizada no es entera.

v_num1 = int(input('Ingrese primer número: '))
v_num2 = int(input('Ingrese segundo número: '))

cociente = v_num1 // v_num2
residuo = v_num1 % v_num2

if v_num1 > v_num2:
    print('El primer número: {} es mayor al segundo: {}'.format(v_num1, v_num2))
    if residuo >= 0 and residuo < v_num2:
        print('Es una div entera, su cociente es: {}'.format(cociente))
    else:
        print('La div no es entera, su cociente es: {} y su residuo es: {}'.format(cociente, residuo))

elif v_num1 == v_num2:
    print('El primer número: {} es igual al segundo: {}'.format(v_num1, v_num2))
    if residuo >= 0 and residuo < v_num2:
        print('Es una div entera, su cociente es: {}'.format(cociente))
    else:
        print('La div no es entera, su cociente es: {} y su residuo es: {}'.format(cociente,residuo))

else:
    print('El primer número no es mayor que el segundo')
    print('La div no es entera, su cociente es: {} y su residuo es: {}'.format(cociente, residuo))
