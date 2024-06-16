import random
n = 0
r = 1
while n != r:
    n = int(input('Tente adivinhar o numero que estou pensando de 1 a 10: '))
    r = random.randint(1, 10)
    if n != r:
        print('Número incorreto, tente novamente! o numero correto era {}'.format(r))
print('Parabens, voce adivinhou o numero corretamente!')
