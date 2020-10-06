'''Escribir una función que reciba otra función booleana y una lista,
y devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.'''

''''# Sol 1

def f_bool(funcion,lista):

    lp = []
    li = []

    for i in lista:
        if funcion(i):
            lp.append(i)
        else:
            li.append(i)
    return lp


def f_par(n):
    return n % 2 == 0

print(f_bool(f_par,[1,2,3,4,5,6]))'''

# Sol 2

def f_bool(funcion,lista):

    lp = []

    for i in lista:
        lp.append(funcion(i))
    return lp

def f_par(n):
    return n % 2 == 0

print(f_bool(f_par,[1,2,3,4,5,6]))