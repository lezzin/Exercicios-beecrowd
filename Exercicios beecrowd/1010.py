valor1 = input().split(" ")
valor2 = input().split(" ")

a1, b1, c1 = valor1
a2, b2, c2 = valor2

soma = ((float(c1)*int(b1))+(float(c2)*int(b2)))

print("VALOR A PAGAR: R$ %.2f" % soma)
