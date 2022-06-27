valores = int(input())
s = 0
n = 0

for i in range(1, valores+1):
    numero = int(input())
    if 10 <= numero <= 20:
        s = s + 1
    else:
        n = n + 1

print("{} in".format(s))
print("{} out".format(n))