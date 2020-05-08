
v_humano = str('ser')
dic = {43104268 : {'nombre':'efrain', 'edad':34, v_humano: 'bebe'=='bebe'},43104269 : {'nombre':'felipe', 'edad':3, v_humano: 'bebe'=='bebe' }}

print(dic)

for keys, values in dic.items():

    # print(values['ser'])

    if values[v_humano]:
        print("if" + str(keys))
    else:
        print("mal")


    # print(i)

# for keys,values in dic.items():
    # print("1 for: " + str(keys), values['nombre'])

# for keys, values in dic.get(43104269).items():
    # if values == 'True':
        # print("es true")
    # else:
        # print("es false")

    # print(keys)
    # if values['bebe'] == 'S':
        # print("es true")
    # else:
        # print("es false")
    # print("2 for: " + str(keys), values)
