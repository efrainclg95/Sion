# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en
# formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

v_fecha = str(input("Introduce una fecha en formato dd/mm/aaaa: "))
lista = v_fecha.split('/')
dic = {'01' : "Enero", '02' : "Febrero", '03' : "Marzo", '04' : "Abril", '05' : "Mayo", '06' : "Junio", '07' : "Julio", '08' : "Agosto", '09' : "Septiembre", '10' : "Octubre", '11' : "Noviembre", '12' : "Diciembre"}

print(lista[0] + " de " + dic.get(lista[1]) + " de " + lista[2])