# Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
# Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su DNI,
# y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
# donde preferente tendrá el valor True si se trata de un cliente preferente.
# El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar.
# En función de la opción elegida el programa tendrá que hacer lo siguiente:
#
# Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
# Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# Preguntar por el NIF del cliente y mostrar sus datos.
# Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
# Terminar el programa.

dic_cliente = {}
v_opcion = ''

print("Opciones")

while v_opcion != 6:
    v_opcion = int(input("(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar todos los clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción: "))
    if v_opcion == 1:
        v_dni = int(input("Ingrese DNI de cliente: "))
        v_nombre = str(input("Ingrese Nombre de cliente: "))
        v_direccion = str(input("Ingrese Dirección de cliente: "))
        v_telefono = int(input("Ingrese Teléfono de cliente: "))
        v_correo = str(input("Ingrese E-mail de cliente: "))
        v_preferente = str(input("Es cliente Preferente S/N: ").upper())

        dic_cliente[v_dni] = {'Nombre':v_nombre,'Dirección':v_direccion,'Teléfono':v_telefono,'Correo':v_correo,'Preferente': v_preferente == 'S'}

        print("Lista de Cliente: " + str(dic_cliente))

    elif v_opcion == 2:
        v_dni = int(input("Ingrese DNI de cliente a Eliminar: "))
        del dic_cliente[v_dni]

    elif v_opcion == 3:
        v_dni = int(input("Ingrese DNI de cliente para mostrar sus datos: "))

        for i in dic_cliente[v_dni]:
            print(str(i) + ": " + str(dic_cliente[v_dni].get(i)))

    elif v_opcion == 4:

        # for j in dic_cliente:
            # print(str(j) + ": " + str(dic_cliente[j].get('Nombre')))

        for keys,values in dic_cliente.items():
            print(keys, values['Nombre'])

    elif v_opcion == 5:

        for keys,values in dic_cliente.items():
            if values['Preferente']:
                print(keys,values['Nombre'])

    elif v_opcion == 6:
        break





