num = int(input())

ano = num//365
num = num-ano*365
mes = num//30
num = num-mes*30
dia = num

print("{} ano(s)".format(ano))
print("{} mes(es)".format(mes))
print("{} dia(s)".format(dia))
