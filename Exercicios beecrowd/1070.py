num = int(input())
impares = []

for n in range(num, num+12):
    if n % 2 != 0:
        impares.append(n)

for n in impares:
    print(n)