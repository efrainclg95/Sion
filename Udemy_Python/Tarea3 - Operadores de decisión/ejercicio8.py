# Haz que un usuario introduzca una palabra y comprueba si dicha palabra empieza por mayúscula. Devuelve
# por pantalla el resultado en cada caso.

v_palabra = str(input('Ingrese palabra: '))

print('la primera letra empieza con mayúscula') if v_palabra[0] == v_palabra[0].upper() else print('la primera letra NO empieza con mayúscula')