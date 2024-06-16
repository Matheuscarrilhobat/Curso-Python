n1 = 0
n2 = 0
n3 = 0
c = 0
while n1 != 999:
    n1 = int(input('Digite um número(digite 999 para encerrar o programa: '))
    if n1 != 999:
     n3 = n1 + n2
     n2 += n1
     c += 1
print('Quantidade de numeros digitados: {} '.format(c))
print('Soma de todos os termos: {} '.format(n3))