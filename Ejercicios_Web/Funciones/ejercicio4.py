# Escribir una función que calcule el total de una factura tras aplicarle el IVA.
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura.
# Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

x = float(input("Ingrese cantidad monetaria actual: "))


def operacion(x,y = 21):
    if y == 21:
        return "Facturación Total IVA 21%: " + str(x + x * y / 100)
    else:
        return "Facturación Total IVA " + str(y) + "%: " + str(x + x * y / 100)

print(operacion(x))
print(operacion(x,40))





"""def invoice(amount, vat=21):
    # Función de aplica el IVA a una factura.
    # Parametros
    # amount: Es la cantidad sin IVA
    # vat: Es el porcentaje de IVA
    #Devuelve el total de la factura una vez aplicado el IVA.
    
    return amount + amount*vat/100

print(invoice(1000,10))
print(invoice(1000))"""