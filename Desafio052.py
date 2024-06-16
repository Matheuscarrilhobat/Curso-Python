num = int(input('Digite um Número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print(end='')
        tot += 1
    else:
        print(end='')
    print(f'{c}', end='')
print('\nO Número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('Por isso ele é PRIMO!')
else:
    print('Por isso ele NÃO É PRIMO!')