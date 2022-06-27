n = input().split(" ")
a, b, c = n
a = float(a)
b = float(b)
c = float(c)

delta = (b**2)-4*a*c

if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    r1 = (-b + delta ** (1/2)) / (2*a)
    r2 = (-b - delta ** (1/2)) / (2*a)
    r1 = ('%.5f' % r1)
    r2 = ('%.5f' % r2)

    print('R1 = {}'.format(r1))
    print('R2 = {}'.format(r2))
