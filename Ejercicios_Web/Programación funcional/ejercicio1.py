'''Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.
scribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la compra,
y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el IVA a los productos de la cesta y
devolver el precio final de la cesta.'''

def apply_IVA(price, percentage):
    return price + (price * percentage)/100

print('IVA: ',apply_IVA(1000,20))

def price_basket(basket, function):
    total = 0
    for price, discount in basket.items():
        # print(price,discount)
        total = total + function(price, discount)
    return total

print(price_basket({1000:20,500:10,100:1},apply_IVA))
