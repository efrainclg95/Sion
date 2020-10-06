"""Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en
formato dd de <mes> de aaaa donde <mes> es el nombre del mes."""

def fecha(dia,mes,año):
    dic = {'01':'Enero','02':'Febrero','03':'Marzo','04':'Abril','05':'Mayo','06':'Junio','07':'Julio','08':'Agosto','09':'Setiembre','10':'Octubre','11':'Noviembre','12':'Diciembre'}
    cadena = str(dia) + ' de ' + str(dic.get(mes)) + ' de ' + str(año)
    return cadena

print(fecha(12,'06',1985))