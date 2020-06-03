
area = lambda base, altura : base * altura
# print(area(4,5))

def cuadrado(n):
    return n * n

# print(tuple(map(cuadrado, [1,2,3])))

def rectangulo(b,h):
    return b * h

# print(list(map(rectangulo, [1,2,3],[4,5,6])))

def par(n):
    return n % 2 == 0

# print(list(filter(par, range(8))))

asignaturas = ['matematicas','fisica','quimica','economia']
notas = [12,8.5,14,12]

# print(dict(zip(asignaturas,notas)))

binomio_cuadrado = lambda a,b : a**2 + 2*a*b + b**2
binomio_cuadrado(2,3)

# print(binomio_cuadrado(2,3))

area_triangulo = lambda base,altura : (base * altura)/2
# print(area_triangulo(7,5))
# print(area_triangulo(9,12343434))

