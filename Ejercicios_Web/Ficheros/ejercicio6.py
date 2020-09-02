'''Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa.
El programa incorporar funciones crear el fichero con el listín si no existe, para consultar el teléfono de un cliente,
añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente.
El listín debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente y
su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.'''

# Sol1

def f_menu():
    print('\nGestión del listin telefónico')
    print('-----------------------------')
    print('1. Consultar un teléfono')
    print('2. Añadir un teléfono')
    print('3. Eliminar un teléfono')
    print('4. Crear el listin')
    print('0. Terminar\n')
    global v_option
    v_option = int(input('Ingrese el número de la opción: '))
    return v_option

def f_bucle(option):
    print('Opción ingresada -->', v_option)

    while v_option == 0 or v_option == 1 or v_option == 2 or v_option == 3 or v_option == 4:

        if v_option == 1:
            f_option1()
            f_bucle(f_menu())

        elif v_option == 2:
            f_option2()
            f_bucle(f_menu())

        elif v_option == 3:
            f_option3()
            f_bucle(f_menu())

        elif v_option == 4:
            f_option4()
            f_bucle(f_menu())

        elif v_option == 0:
            print('Hasta pronto amiguitos')
        break

def f_option1():
    print('opcion 1')

def f_option2():
    print('opcion 2')

def f_option3():
    print('opcion 3')

def f_option4():
    print('opcion 3')

print(f_bucle(f_menu()))
# print(f_option1())
