'''Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa.
El programa incorporar funciones crear el fichero con el listín si no existe, para consultar el teléfono de un cliente,
añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente.
El listín debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente y
su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.'''

# Sol1

dic = {}

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
        file = open('listin.txt', 'r')
    except FileNotFoundError:
        print('El fichero no existe :(')
    else:
        file = open('listin.txt','r')
        file_list = file.readlines()

        for i in file_list:
            file_list = i.split(',')
            for j,k in enumerate(file_list):
                dic[file_list[0]] = file_list[1]
        print('Su teléfono es: ',dic.get(customer_name))

def f_option2():

    customer_name = str(input('Ingrese nombre de cliente: '))
    telephone_number = int(input('Ingrese número telefónico: '))

    add(customer_name,telephone_number)
    print('Cliente añadido a Base de Datos: ', add(customer_name, telephone_number))

    for keys,values in add(customer_name, telephone_number).items():

        f_option4()

        file = open('listin.txt','a')
        file.write(str(keys) + ',' + str(values) + '\n')


def f_option3():

    print('opt3')

def f_option4():

    file = open('listin.txt','w')
    # file.write('Lista Telefonica\n')

def add(customer_name,telephone_number):

    dic[customer_name] = telephone_number
    return dic

print(f_bucle(f_menu()))
