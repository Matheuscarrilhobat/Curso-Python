pre = float(input('Insira o Valor do Produto:'))
pag = int(input('Insira Forma de Pagamento:\n1-a Vista no Dinheiro\n2-A Vista no Cartão\n3-em até 2x no Cartão\n4- 3x ou mais no Cartão\n'))

if pag == 1:
    pre -= pre * 0.10
    print('Valor a ser Pago:R${}'.format(pre))
elif pag == 2:
    pre -= pre * 0.05
    print('Valor a ser Pago:R${}'.format(pre))
elif pag == 3:
    print('Valor a ser Pago:R${}'.format(pre))
elif pag == 4:
    pre += pre * 0.20
    print('Valor a ser Pago:R${}'.format(pre))