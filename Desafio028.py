import random
n = int(input('Tente Adivinhar o numero que estou pensando de 1 a 10: '))
r = random.randint(1, 10)
if n == r:
    print('Parabens, você adivinhou o numero corretamente!')
else:
    print('Numero Incorreto, tente novamente! o numero correto era {}'.format(r))