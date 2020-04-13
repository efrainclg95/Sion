# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

diccionario = {'Euro' : ['€'],
               'Dollar': ['$'],
               'Yen' : ['¥']
               }

v_divisa = str(input("Ingrese Divisa: "))

if v_divisa == 'Euro' or v_divisa == 'Dollar' or v_divisa == 'Yen' :
    print("Su símbolo es: " + str(diccionario[v_divisa]))

else:
    print("La Divisa ingresada no existe en el diccionario")


