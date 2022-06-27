numero = int(input())

hora = numero // 3600
numero = numero - hora * 3600

minutos = numero // 60
numero = numero - minutos*60
segundos = numero

print('%.0f:%.0f:%.0f' % (hora, minutos, segundos))
