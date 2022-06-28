t = int(input())
comp = input().split()
a, b, c, d, e = comp
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
i = 0

if a == t:
    i += 1
if b == t:
    i += 1
if c == t:
    i += 1
if d == t:
    i += 1
if e == t:
    i += 1
print(i)
