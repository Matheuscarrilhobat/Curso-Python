valores = []
while True:
    valores.append(int(input('Digite um Valor: ')))
    resp = str(input('Quer Continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} Elementos')
valores.sort(reverse=True)
print(f'Os Valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista!')

