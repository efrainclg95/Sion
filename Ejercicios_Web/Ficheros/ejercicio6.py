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
    print('Opción ingresada -->', option)

    while option == 0 or option == 1 or option == 2 or option == 3 or option == 4:

        if option == 1:
            f_option1()
            f_bucle(f_menu())

        elif option == 2:
            f_option2()
            f_bucle(f_menu())

        elif option == 3:
            f_option3()
            f_bucle(f_menu())

        elif option == 4:
            f_option4()
            f_bucle(f_menu())

        elif option == 0:
            print('Hasta la vista baby')
        break

    else:
        print('Ingrese una opción válida')
        f_bucle(f_menu())


def f_option1():
    customer_name = str(input('Introduce el nombre del cliente: '))
    try:
        file = open('listin.txt')
    except FileNotFoundError:
        print('El fichero no existe :(')
    else:
        print(file.read())




def f_option2():
    print('opcion 2')

def f_option3():
    print('opcion 3')

def f_option4():
    # print('opcion 4')
    file = open('listin.txt','w')
    file.write('efrain,963752034') # escritura en duro para pruebas


print(f_bucle(f_menu()))


