'''Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa.
El programa incorporar funciones crear el fichero con el listín si no existe, para consultar el teléfono de un cliente,
añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente.
El listín debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente y
su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.'''

# Sol1
import os

dic = {}
# customer_name = ''
# telephone_number = int

def f_menu():

    print('\nGestión del listin telefónico')
    print('-----------------------------')
    print('1. Consultar un teléfono')
    print('2. Añadir un teléfono')
    print('3. Eliminar un teléfono')
    print('4. Crear\Actualizar el listin')
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
    return

# funciones principales

def f_option1():

    try:
        file = open('listin.txt')
    except FileNotFoundError:
        print('El fichero no existe')
    else:
        customer_name = str(input('Ingrese nombre de cliente: '))

        file = open('listin.txt','r')
        file_list = file.readlines()

        lookup_dic = {}

        for j,k in enumerate(file_list):
            file_list = k.split(',')

            lookup_dic[file_list[0]] = file_list[1]

        if customer_name in lookup_dic:
            print('Su teléfono es: ',lookup_dic.get(customer_name))
        else:
            print('El cliente ingresado no existe en base')

def f_option2():

    add_data()

    return

def f_option3():

    customer_name = str(input('Ingrese nombre de cliente a eliminar: '))

    file = open('listin.txt', 'r')
    file_list = file.readlines()

    lookup_dic = {}

    for j, k in enumerate(file_list):
        file_list = k.split(',')

        lookup_dic[file_list[0]] = file_list[1]

    lookup_dic.pop(customer_name)
    # print(lookup_dic)

    print('Se procede a la actualización del listin')
    file = open('listin.txt', 'w')
    for keys, values in lookup_dic.items():
        file.write(str(keys) + ',' + str(values))
    file.close()

def f_option4():

    path = 'C:/Users/Efraín/PycharmProjects/Sion/Ejercicios_Web/Ficheros'

    if 'listin.txt' in os.listdir(path):
        print('Ya existe listin.txt, se procede a la actualización')

        # Proceso de análisis de listin

        file = open('listin.txt', 'r')
        file_list = file.readlines()

        lookup_dic = {}

        for j, k in enumerate(file_list):
            file_list = k.split(',')

            lookup_dic[file_list[0]] = file_list[1]

        # print(lookup_dic)
        # print(dic)

        # Actualiza listin

        lookup_dic.update(dic)

        file = open('listin.txt', 'w')
        for keys, values in lookup_dic.items():
            file.write(str(keys) + ',' + str(values) + '\n')
        file.close()

    else:
        print('Listin no existe, se procede a la creación')
        file = open('listin.txt', 'w')
        for keys, values in dic.items():
            file.write(str(keys) + ',' + str(values) + '\n')
        file.close()

    return

# funciones de apoyo

def add_data():

    # print('log,ingresa add_data')

    customer_name = str(input('Ingrese nombre de cliente: '))
    telephone_number = int(input('Ingrese número telefónico: '))

    base(customer_name,telephone_number)

    return

def base(customer_name,telephone_number):

    # print('log,ingresa base')

    dic[customer_name] = telephone_number
    print(dic)

    return

def read():

    file = open('listin.txt','r')
    content = file.read()
    return content

print(f_bucle(f_menu()))


