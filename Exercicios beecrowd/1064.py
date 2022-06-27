lista = []
pos = 0
for x in range(1, 7):
    num = float(input())
    if num > 0:
        pos = pos+1
        lista.append(num)
        lista2 = sum(lista)/len(lista)
print("{} valores positivos".format(pos))
print("{:.1f}".format(lista2))
