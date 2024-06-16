import random

play = input('Insira Pedra, Papel ou Tesoura: ')
cpu = random.randint(1,3)
play = play.upper()
if cpu == 1:
    print('Pedra!')
elif cpu == 2:
    print('Papel!')
else:
    print('Tesoura!')
if play == 'PEDRA' and cpu == 1:
    print('Empate!')
elif play == 'PEDRA' and cpu == 2:
    print('Derrota!')
elif play == 'PEDRA' and cpu == 3:
    print('Vitória!')
elif play == 'PAPEL' and cpu == 1:
    print('Vitória!')
elif play == 'PAPEL' and cpu == 2:
    print('Empate!')
elif play == 'PAPEL' and cpu == 3:
    print('Derrota')
elif play == 'TESOURA' and cpu == 1:
    print('Derrota!')
elif play == 'TESOURA' and cpu == 2:
    print('Vitória')
elif play == 'TESOURA' and cpu == 3:
    print('Empate!')
else:
    print('Erro!')