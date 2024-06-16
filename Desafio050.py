s = 0
for c in range(0, 6):
    n = int(input('Insira um valor: '))
    if n % 2 == 0:
        s += n
print('Total da soma dos valores pares: {}'.format(s))
