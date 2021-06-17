# Haz que el usuario introduzca precios por teclado (si introduce 0, entonces es que ha finalizado). Si el usuario
# pasa de 200€, entonces ya no debe poder introducir más precios pues se ha pasado de presupuesto. Sea cual
# sea el resultado (o bien el precio final o bien que no tiene más presupuesto), indícaselo por pantalla al usuario.

v_precio = float(input('Ingrese precio: '))

while v_precio != 0:
    if v_precio < 200:
        v_precio = float(input('Ingrese precio: '))
    else:
        print('Ya no puedes ingresar precios')
        break
else:
    print('Ya no puedes ingresar precios')


