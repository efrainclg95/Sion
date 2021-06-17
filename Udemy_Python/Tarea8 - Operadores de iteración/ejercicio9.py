# Haz que el usuario introduzca su edad y el año actual. Imprime todos los años que han pasado desde su año
# de nacimiento hasta el año actual (ambos incluidos).

v_edad = int(input('Ingrese su edad: '))
v_ano = int(input('Ingrese año actual: '))

v_nacimiento = v_ano - v_edad
# print('Año de nacimiento: ',v_nacimiento)

for anos in range(v_nacimiento,v_ano + 1):
    print(anos)