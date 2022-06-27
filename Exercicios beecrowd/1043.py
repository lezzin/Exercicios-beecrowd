valores = input().split()
a, b, c = valores
a = float(a)
b = float(b)
c = float(c)

if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    perimetro = a+b+c
    print('Perimetro = {:.1f}'.format(perimetro))
else:
    area = ((a + b) / 2) * c
    print('Area = {:.1f}'.format(area))
