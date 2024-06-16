import datetime
from time import strftime

nasc = int(input('Insira seu ano de Nascimento: '))
ano = datetime.date.today()
idade = int(ano.strftime('%Y')) - nasc
if idade > 18:
    dif = idade - 18
    print('Seu Prazo de Alistamento terminou a {} anos'.format(dif))
elif idade < 18:
    dif = 18 - idade
    print('Você deve se Alistar daqui a {} ano(s)'.format(dif))
else:
    print('Você deve se Alista este ano!')