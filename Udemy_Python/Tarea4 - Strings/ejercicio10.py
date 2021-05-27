# Con lo hecho en los ejercicios 6, 7, 8 y 9, imprime por pantalla todos los datos introducidos por el usuario
# tal y como se muestra en el siguiente ejemplo, donde el usuario ha indicado que su nombre es María; su
# apellido, Santos; su edad, 21; y su ciudad, Palma de Mallorca.
# Su nombre es María Santos, tiene 21 años y actualmente vive en Palma de Mallorca.

v_nombre = input('Introduzca su nombre: ')
v_apellido = input('Introduzca su apellido: ')
v_edad = int(input('introduzca su edad: '))
v_ciudad = input('Introduzca la ciudad donde vive: ')

print('Su nombre es ' + v_nombre + ' ' + v_apellido + ', tiene ' + str(v_edad) + ' años y actualmente vive en ' + v_ciudad + '.')