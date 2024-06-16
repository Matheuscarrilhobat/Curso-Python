n1 = 0
n2 = 0
n3 = 0
c = 0
resp = '0'
mai = 0
men = 99999999999999
while resp != 'N':
    n1 = int(input('Insira um Número: '))
    n3 = n1 + n2
    n2 += n1
    c += 1
    if mai < n1:
        mai = n1
    if men > n1:
        men = n1
    resp = input('Deseja continuar? [S/N]: ').upper()
med = n3/c
print('Média dos valores digitados: {}'.format(med))
print('Maior valor encontrado: {}'.format(mai))
print('Menor valor encontrado: {}'.format(men))
