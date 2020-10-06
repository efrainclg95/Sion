
"""Ejemplos lambda"""

binomio_cuadrado = lambda a,b : a**2 + 2*a*b + b**2
binomio_cuadrado(2,3)

# print(binomio_cuadrado(2,3))

area_triangulo = lambda base,altura : (base * altura)/2
# print(area_triangulo(7,5))
# print(area_triangulo(9,12343434))

area = lambda base, altura : base * altura
# print(area(4,5))


"""Ejemplos map"""

def cuadrado(n):
    return n * n

# print(tuple(map(cuadrado, [4,5])))

def rectangulo(b,h):
    return b * h

# print(list(map(rectangulo, [1,2,3],[4,5,6])))

"""Ejemplos filter"""

def par(n):
    return n % 2 == 0

# print(list(filter(par, range(8))))

lista = [-1,0,1,2,5]
def filtro(n):
    return n > 0

# print(list(filter(filtro,lista)))


"""Ejemplos zip"""

asignaturas = ['matematicas','fisica','quimica','economia']
notas = [12,8.5,14,12]

# print(dict(zip(asignaturas,notas)))

"""Funcion reduce"""

import functools

def multiplicar(x, y):
    # print(x * y)  # muestra el resultado parcial
    return x * y

lista = [1, 2, 3, 4]
valor = functools.reduce(multiplicar, lista)
print(valor)  # muestra el resultado final

def producto(n,m):
    return n * m

# print(functools.reduce(producto, range(1,5)))