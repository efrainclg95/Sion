# Haz que un usuario introduzca su nombre y evalúa con operadores if y else si dicho nombre tiene una
# longitud mayor a 10 caracteres o no. Devuelve por pantalla el resultado en cada caso.

v_nombre = input('ingrese su nombre: ')

if len(v_nombre) >= 10:
    print('Su longitud es mayor a 10')
else:
    print('Su longitud es menor a 10')
