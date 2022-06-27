valor = int(input())

for i in range(1, valor+1):
    n = input().split()
    a,b = n
    a=int(a)
    b=int(b)

    if b == 0:
        print("divisao impossivel")
    if b != 0:
        c = a / b
        print("{}".format(c))