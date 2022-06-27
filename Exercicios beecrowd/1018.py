numero = int(input())
print(numero)
cem = numero // 100
numero = numero - cem*100

cinquenta = numero // 50
numero = numero - cinquenta*50

vinte = numero // 20
numero = numero - vinte*20

dez = numero // 10
numero = numero - dez*10

cinco = numero // 5
numero = numero - cinco*5

dois = numero // 2
numero = numero - dois*2

um = numero // 1
numero = numero - um*1
print('{} nota(s) de R$ 100,00'.format(cem))
print('{} nota(s) de R$ 50,00'.format(cinquenta))
print('{} nota(s) de R$ 20,00'.format(vinte))
print('{} nota(s) de R$ 10,00'.format(dez))
print('{} nota(s) de R$ 5,00'.format(cinco))
print('{} nota(s) de R$ 2,00'.format(dois))
print('{} nota(s) de R$ 1,00'.format(um))
