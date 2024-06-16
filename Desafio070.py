tot = 0
mil = 0
menpre = 999999999999999999999999
mennom = ''
while True:
    nom = input('Insira o nome do produto: ')
    pre = float(input('Insira o preço do produto: '))
    tot += pre
    if pre > 1000:
        mil += 1
    if pre < menpre:
        menpre = pre
        mennom = nom
    resp = input('Deseja Continuar? [S/N]')
    resp = resp.upper()
    if resp == 'N':
        break
print(f'Total Gasto: R${tot:.2f}')
print(f'Total de Produtos que custam acima de R$1000: {mil}')
print(f'Produto mais Barato: {mennom} R${menpre:.2f}')