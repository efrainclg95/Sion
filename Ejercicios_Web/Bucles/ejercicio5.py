# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
# y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))

for i in range(years):
    amount *= 1 + interest / 100
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 3)))