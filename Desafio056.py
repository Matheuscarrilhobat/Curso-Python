mul = 0
med = 0
pidade = 0
for c in range(0, 4):
    nome = input('Insira seu Nome: ')
    idade = int(input('Insira sua Idade: '))
    sexo = input('Insira seu Sexo: ')
    med += idade
    if idade > pidade and sexo == 'M':
        vel = nome
    pidade = idade
    if idade < 20 and sexo == 'F':
        mul += 1
med = med/4
print('A Média de idade é {}'.format(med))
print('O Homem mais velho é {}'.format(vel))
print('Existem {} mulheres com menos de 20 anos'.format(mul))
