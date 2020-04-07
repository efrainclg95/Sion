# Escribir un programa que pregunte por una muestra de números, separados por comas,
# los guarde en una lista y muestre por pantalla su media y desviación típica.

v_num = input("Introduce una muestra de números separados por comas: ")

# v_num = str("4,3,5,8,5,2,3,5")
v_num = v_num.split(",")
v_ancho = len(v_num)
v_media = float(0)

for i in range(v_ancho):
    v_media = float(v_media) + int(v_num[i])/v_ancho

print("La media es: " + str(v_media))










