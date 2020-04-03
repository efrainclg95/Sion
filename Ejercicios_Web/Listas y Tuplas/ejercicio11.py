# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

v1 = (1,2,3)
v2 = (-1,0,2)
lv1 = []
lv2 = []
p = int(0)

for i in v1:
    lv1.append(i)

for j in v2:
    lv2.append(j)

for k in range(len(lv1)):
    p = (lv1[k]*lv2[k]) + p
print("El producto escalar es: " + str(p))

# Sol1

# for i in v1:
    # lv1.append(i)
# print(lv1)

# for j in v2:
    # lv2.append(j)
# print(lv2)

# p = (lv1[0] * lv2[0]) + (lv1[1] * lv2[1]) + (lv1[2] * lv2[2])
# print(p)

# Sol2
