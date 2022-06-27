valor = int(input())
lista = ['']
for i in range(1, valor + 1):
    lista.append(int(input()))
   
for i in range(1, valor + 1):
    if lista[i] == 0:
        print('NULL')
       
    if lista[i] > 0:
        if lista[i] % 2 == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')
           
    if lista[i] < 0:
        if lista[i] % 2 == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')