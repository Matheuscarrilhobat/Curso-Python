val = float(input('Insira o valor da Casa:'))
sal = float(input('Insira o salário do comprador:'))
ano = int(input('Insira a quantidade de anos que levará para pagar:'))

anual = val / ano
pres = anual / 30
lim = sal * 0.30

if lim <= pres:
    print('Empréstimo Aprovado')
else:
    print('Empréstimo Recusado')
