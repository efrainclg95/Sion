ejemplo = [3,7,9,5,3,7,12]

lp = []
li = []

for i in ejemplo:
    if i % 2 == 0:
        lp.append(i)
    else:
        li.append(i)
        li.sort()

print(lp,li)
