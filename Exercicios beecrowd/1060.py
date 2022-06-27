par = 0
impar = 0
pos = 0
neg = 0
for x in range(1, 6):
    a = int(input())
    if a % 2 == 0:
        par = par + 1
    if a % 2 != 0:
        impar = impar+1
    if a > 0:
        pos = pos+1
    if a < 0:
        neg = neg+1

print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(impar))
print('{} valor(es) positivo(s)'.format(pos))
print('{} valor(es) negativo(s)'.format(neg))
