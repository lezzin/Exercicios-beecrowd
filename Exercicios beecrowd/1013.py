valor = input().split(" ")
a, b, c = valor

maior = (int(a)+int(b)+abs(int(a)-int(b)))/2
maior2 = (int(c)+int(maior)+abs(int(c)-int(maior)))/2
print("%d eh o maior" % maior2)
