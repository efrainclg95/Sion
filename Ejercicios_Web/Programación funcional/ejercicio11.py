"""Escribir una función que reciba una muestra de números y
devuelva los valores atípicos, es decir,
los valores cuya puntuación típica sea mayor que 3 o menor que -3.
Nota: La puntuación típica de un valor se obtiene
restando la media y dividiendo por la desviación típica de la muestra."""

from statistics import mean, stdev

def atipico(muestra):
    media = mean(muestra)
    desviacion = stdev(muestra)
    def f(n):
        puntuacion = (n - media) / desviacion
        return (puntuacion < -3) or (puntuacion > 3)
    return f

def datos_atipicos(muestra):
    return list(filter(atipico(muestra), muestra))

print(datos_atipicos([1,2,3,4,5,6,7,8,9,10,1000]))




