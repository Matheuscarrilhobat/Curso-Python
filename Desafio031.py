d = float(input('Insira a Distancia da Viagem: '))
if d <= 200:
    p = d * 0.50
    print('Valor de Passagem: R${}'.format(p))
else:
    p = d * 0.45
    print('Valor da Passagem para viagens acima de 200km: R${}'.format(p))