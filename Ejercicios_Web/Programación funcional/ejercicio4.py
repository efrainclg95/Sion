'''Escribir una función que reciba otra función booleana y una lista,
y devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.'''

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

# print(f_par(5))

print(f_bool(f_par,[1,2,3,4,5,6]))