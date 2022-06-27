valor = int(input())

for i in range(1, valor+1):
    if i % 2 == 0:
        r=i**2
        print("{}^2 = {}".format(i,r))
