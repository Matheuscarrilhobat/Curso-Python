n1 = int(input('Insira o primeiro numero: '))
n2 = int(input('Insira o segundo numero: '))
n3 = int(input('Insira o terceiro numero: '))
if n1 > n2 and n1 > n3:
    print('Maior Numero: {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('Maior Numero: {}'.format(n2))
if n3 > n1 and n3 > n2:
    print('Maior Numero: {}'.format(n3))