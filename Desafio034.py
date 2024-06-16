s = float(input('Insira o valor de seu Salário: '))
if s > 1250:
    s = s + (s * 0.10)
    print('Novo Salário: R${:.2f}'.format(s))
else:
    s = s + (s * 0.15)
    print('Novo Salário: R${:.2f}'.format(s))