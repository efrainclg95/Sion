"""Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario."""


v_divisa = str(input("Indique divisa:\n- Euro\n- Dollar\n- Yen\nEscriba: "))

def divisa(v_divisa):
    dic = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    return list(dic.get(v_divisa))

print(divisa(v_divisa))








