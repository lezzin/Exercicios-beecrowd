valor = int(input())

for i in range(1,valor+1):
    valores = input().split(" ")
    a,b,c = valores
    a=float(a)
    b=float(b)
    c=float(c)
    print('{:.1f}'.format((a * 2 + b * 3 + c * 5) / 10))