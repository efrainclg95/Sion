# Haz que el usuario introduzca un número entero. Muestra un cuadrado y luego un triángulo rectángulo de
# lado y altura, respectivamente, el número entero introducido. Por ejemplo, si el usuario introduce como
# número 5, se deberá mostrar:

# *             * * * * *
# * *           * * * * *
# * * *         * * * * *
# * * * *       * * * * *
# * * * * *     * * * * *

altura = int(input("Altura del triángulo: "))

for i in range(1, altura + 1):
    for j in range(i):
        print("* ", end="")
    print()


for i in range(altura):
    print('*' * altura)

