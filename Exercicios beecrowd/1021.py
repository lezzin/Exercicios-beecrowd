numero = float(input())
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
um = float('%.2f' % um)
numero = float('%.2f' % numero)

cent50 = numero // 0.5
numero = numero - cent50*0.5
cent50 = float('%.2f' % cent50)
numero = float('%.2f' % numero)

cent25 = numero // 0.25
numero = numero - cent25*0.25
cent25 = float('%.2f' % cent25)
numero = float('%.2f' % numero)

cent10 = numero // 0.10
numero = numero - cent10*0.10
cent10 = float('%.2f' % cent10)
numero = float('%.2f' % numero)

cent5 = numero // 0.05
numero = numero - cent5*0.05
cent5 = float('%.2f' % cent5)
numero = float('%.2f' % numero)

cent1 = numero * 100
cent1 = float('%.2f' % cent1)
numero = float('%.2f' % numero)

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(cem)))
print('{} nota(s) de R$ 50.00'.format(int(cinquenta)))
print('{} nota(s) de R$ 20.00'.format(int(vinte)))
print('{} nota(s) de R$ 10.00'.format(int(dez)))
print('{} nota(s) de R$ 5.00'.format(int(cinco)))
print('{} nota(s) de R$ 2.00'.format(int(dois)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00' .format(int(um)))
print('{} moeda(s) de R$ 0.50'.format(int(cent50)))
print('{} moeda(s) de R$ 0.25'.format(int(cent25)))
print('{} moeda(s) de R$ 0.10'.format(int(cent10)))
print('{} moeda(s) de R$ 0.05'.format(int(cent5)))
print('{} moeda(s) de R$ 0.01'.format(int(cent1)))
