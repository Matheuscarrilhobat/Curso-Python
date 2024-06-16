import datetime
ma = 0
me = 0
ano = datetime.date.today()
for c in range(0 , 7):
    nasc = int(input('Insira seu Ano de Nascimento: '))
    idade = int(ano.strftime('%Y')) - nasc
    if idade >= 21:
        ma += 1
    else:
        me += 1
print('Existem {} maiores de idade e {} menores de idade'.format(ma, me))
