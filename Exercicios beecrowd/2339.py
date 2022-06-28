n = input().split()
c, p, f = n
c = int(c)
p = int(p)
f = int(f)

if c*f <= p:
    print('S')
else:
    print('N')
