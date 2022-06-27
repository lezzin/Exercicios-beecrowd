N = int(input())
contador = 0
a, b, c = 1, 2, 3
while contador < N:
    print('{0} {1} {2} PUM'.format(a, b, c))
    c += 2
    a = c
    b = c
    b += 1
    c += 2
    contador += 1
