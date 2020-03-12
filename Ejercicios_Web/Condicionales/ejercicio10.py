print("xxxxx BIENVENIDO A PIZZAS FELIPILLO xxxxx \n")
print("Tipos de Pizza: \n 1. Vegetariana \n 2. No Vegetariana  ")
v_tipop = int(input("Escriba el numero de Pizza que desea: "))

if v_tipop == int(1):
    print("Selecciono Vegetariana")
    print("Ingredientes: \n 1. Pimiento \n 2. Tofu ")
    v_ingrediente = int(input("Seleccione un tipo de ingrediente: "))
    if v_ingrediente == int(1):
        print("Pizza Vegetariana con: \n 1. Tomate \n 2. Mozarella \n 3. Pimiento")
    else:
        print("Pizza Vegetariana con: \n 1. Tomate \n 2. Mozarella \n 3. Tofu")
else:
    print("Selecciono No Vegetariana")
    print("Ingredientes: \n 1. Peperoni \n 2. Salmon \n 3. Jamon ")
    v_ingrediente = int(input("Seleccione un tipo de ingrediente: "))
    if v_ingrediente == int(1):
        print("Pizza No Vegetariana con: \n 1. Tomate \n 2. Mozarella \n 3. Peperoni")
    elif v_ingrediente == int(2):
        print("Pizza No Vegetariana con: \n 1. Tomate \n 2. Mozarella \n 3. Salmon")
    else:
        print("Pizza No Vegetariana con: \n 1. Tomate \n 2. Mozarella \n 3. Jamon")





