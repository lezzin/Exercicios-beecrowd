valor = float(input())

if 0 <= valor <= 25:
    print('Intervalo [0,25]')
if 25 < valor <= 50:
    print('Intervalo (25,50]')
if 50 < valor <= 75:
    print('Intervalo (50,75]')
if 75 < valor <= 100:
    print('Intervalo (75,100]')
if valor > 100 or valor < 0:
    print('Fora de intervalo')
