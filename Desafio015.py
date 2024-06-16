km = float(input('Quantos km foram rodados? '))
d = int(input('Quantos dias alugados? '))
tot = (d * 60) + (km * 0.15)
print('Total a pagar:R${:.2f}'.format(tot))