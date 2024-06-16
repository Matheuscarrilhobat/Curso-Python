num = input('Insira um Número entre 0 e 9999: ')
s = '000' + num
uni = s[-1]
dez = s[-2]
cen = s[-3]
mil = s[-4]

print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cen))
print('Milhar: {}'.format(mil))