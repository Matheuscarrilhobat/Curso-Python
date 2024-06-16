v = float(input('Insira a velocidade do carro: '))
if v > 80:
    m = (v - 80) * 7
    print('Limite de Velocidade Ultrapassado! Multa no valor de: R${:.2f}'.format(m))
else:
    print('Dentro do Limite de velocidade.')