


def menu():
    print('Cambio de moneda')
    v_tipo = int(input("1. cambiar a Dolar\n2. cambiar a Euro\nIngrese opción: "))

    global cantidad_soles
    cantidad_soles = float(input("Ingrese su cantidad en S/.: "))

    global precio_dolar
    precio_dolar = float(3.33)

    global precio_euro
    precio_euro = float(3.74)

    if v_tipo == 1:
        dolares()
    elif v_tipo == 2:
        euros()

def dolares():
    ca_dolar = cantidad_soles / precio_dolar
    print("Usted tiene $: " + str(ca_dolar))

def euros():
    ca_euros = cantidad_soles / precio_euro
    print("Usted tiene €: " + str(ca_euros))

menu()







##

"""def f_check(n):
    if n % 2 == 0:
        return 'p'
    else:
        return 'i'

print(f_check(2))"""


"""lista = [2,3,7,9,5,3,7,12]

lp = []
li =[]

def separa_lista(lista):

    for i in lista:
        if i % 2 == 0:
            lp.append(i)
        else:
            li.append(i)
    return lp,li

separa_lista([1,2,3,4,5,6,7,8,9,0])

# lp,li = separa_lista(lista)

print(lp)
print(li)"""

##

"""lista = [2,3,7,9,5,3,7,12]

lp = []
li = []

for i in ejemplo:
    if i % 2 == 0:
        lp.append(i)
    else:
        li.append(i)

print(lp,li)"""



