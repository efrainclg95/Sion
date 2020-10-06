'''otros ejercicios funcionales'''

# lambda

area_cuadrado = lambda lado1,lado2 : lado1*lado2
print('area_cuadrado con lambda: ',area_cuadrado(20,20))

area_rectangulo = lambda base,altura : base*altura
print('area_rectangulo con lambda: ',area_cuadrado(20,500))


# map

def cubo(n):
    return n**3

print('usando map cubo: ',list(map(cubo,[2,3])))

def rectangulo(b,a):
    return b * a

print('usando map rectangulo: ',list(map(rectangulo,[4,5],[2,3])))

# filter

def mayores_n(n):
    return n > 5

print('usando filter mayores a n: ',list(filter(mayores_n,range(10))))

def pares(n):
    return n % 2 == 0

print('usando filter pares n: ',list(filter(pares,range(1,10+1))))

# zip

l0 = ['nombre','ap_paterno','ap_materno']
l1 = ['efrain','lino','gamarra']

print('usando zip: ',dict(zip(l0,l1)))


# reduce

from functools import reduce

def producto(x,y):
    return x * y

print('usando reduce: ',reduce(producto,range(1,5+1)))

# Comprensión de listas

print([x ** 2 for x in range(10)])
print([y for y in range(1,10 + 1) if y % 2 == 0])

notas = {'Carmen':5,'Antonio': 4,'Juan': 8}
print([nombre for nombre,nota in notas.items() if nota >= 5])

# Comprensión de diccionarios

print({palabra:len(palabra) for palabra in ['Felipe', 'bello', 'bebe']})


notas = {'Carmen':5, 'Antonio':4, 'Juan':8, 'Mónica':9, 'María': 6,'Pablo':3}
print({nombre: nota +1 for nombre, nota in notas.items() if nota >= 5})


