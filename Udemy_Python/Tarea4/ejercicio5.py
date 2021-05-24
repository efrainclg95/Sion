# Del string s del ejercicio anterior, obtén el substring chocolate y guárdalo en una variable llamada s_sub.
# No vale contar, deberás hallar los índices del substring con el método .find() (o el que mejor consideres) y
# la función len().
# Finalmente, imprime tu resultado por pantalla

s = "Mi pasión por el chocolate es superior a mis fuerzas"
s_sub = s.find('chocolate')
s_sub = s[s_sub:26]

print(s_sub)


