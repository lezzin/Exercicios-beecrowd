valor = int(input())

if 2 < valor < 1000:
    for n in range(1,11):
        valor2 = valor*n
        print("{} x {} = {}".format(n, valor, valor2))
