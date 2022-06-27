valores = input().split()
cod, quant = valores
if cod == '1':
    print('Total: R$ {:.2f}'.format(4.00*float(quant)))
if cod == '2':
    print('Total: R$ {:.2f}'.format(4.50*float(quant)))
if cod == '3':
    print('Total: R$ {:.2f}'.format(5.00*float(quant)))
if cod == '4':
    print('Total: R$ {:.2f}'.format(2.00*float(quant)))
if cod == '5':
 print('Total: R$ {:.2f}'.format(1.50*float(quant)))
