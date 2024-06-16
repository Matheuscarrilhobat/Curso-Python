import datetime

from time import strftime

nasc = int(input('Insira seu Ano de Nascimento: '))
ano = datetime.date.today()
idade = int(ano.strftime('%Y')) - nasc

if idade < 9:
    print('Atleta Mirim')
elif 9 < idade < 14:
    print('Atleta Infantil')
elif 14 < idade < 19:
    print('Atleta Junior')
elif 19 < idade <= 20:
    print('Atleta Senior')
else:
    print('Atleta Master')
