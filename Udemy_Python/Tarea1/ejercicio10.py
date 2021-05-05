# Ejercicio 10 ¿Cuál es el argumento del número complejo i?:
import cmath

operacion9 = abs((9 - 3j)/(-2-1j))


operacion10 = cmath.phase(operacion9)
print(operacion10)
