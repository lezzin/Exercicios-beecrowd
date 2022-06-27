import math

p1 = input().split(" ")
p2 = input().split(" ")
x1, y1 = p1
x2, y2 = p2

n1 = (float(x2) - float(x1))
n2 = (float(y2)-float(y1))
n3 = ((n1**2)+(n2**2))

distancia = math.sqrt(n3)

print("%.4f" % distancia)
