salario = float(input())

if salario <= 400.00:
    salario2 = salario*1.15
    diferenca = salario2 - salario
    percentual = 15

if 400.01 < salario <= 800.00:
    salario2 = salario*1.12
    diferenca = salario2 - salario
    percentual = 12

if 800.01 <= salario <= 1200.00:
    salario2 = salario*1.10
    diferenca = salario2 - salario
    percentual = 10

if 1200.01 <= salario <= 2000.00:
    salario2 = salario*1.07
    diferenca = salario2 - salario
    percentual = 7

if salario > 2000:
    salario2 = salario*1.04
    diferenca = salario2 - salario
    percentual = 4

print("Novo salario: {:.2f}".format(salario2))
print("Reajuste ganho: {:.2f}".format(diferenca))
print("Em percentual: {} %".format(percentual))
