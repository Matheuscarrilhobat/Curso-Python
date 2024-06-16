num = (int(input('Digite um Número: ')) ,
       int(input('Digite outro Número: ')),
       int(input('Digite mais um Número: ')),
       int(input('Digite o ùltimo Número: ')))
print(f'Você digitou os Valores {num}')
print(f'O Valor 9 apareceu {num.count(9)} vezes')
print(f'O Valor 3 apareceu na {num.index(3)+1} posição')
print('Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')