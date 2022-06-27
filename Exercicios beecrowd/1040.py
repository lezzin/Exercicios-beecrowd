valores = input().split()

n1, n2, n3, n4 = valores
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (n1*2+n2*3+n3*4+n4*1)/10
print("Media: {:.1f}".format(media))
if media >= 7.00:
    print("Aluno aprovado.")
if media < 5.0:
    print("Aluno reprovado.")
if 5.0 <= media <= 6.9:
    print("Aluno em exame.")
    nota = float(input())
    print('Nota do exame: {}'.format(nota))
    media2 = (nota + media) / 2
    if media2 >= 5.0:
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(media2))
    else:
        print("Aluno reprovado.")
        print("Media final: {:.1f}".format(media2))
