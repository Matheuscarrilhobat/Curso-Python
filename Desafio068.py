import random
v = 0
while True:
    pop = input('Par ou Ímpar?')
    pop = pop.upper()
    n = int(input('Insira seu Número(entre 0 e 5): '))
    cpu = random.randint(0, 5)
    s = n + cpu
    print(cpu)
    if pop == 'PAR' and s % 2 != 0:
        print('Você Perdeu!')
        break
    if pop == 'IMPAR' and s % 2 == 0:
        print('Você Perdeu!')
        break
    if pop == 'PAR' and s % 2 == 0:
        print('Você Ganhou!')
        v += 1
    if pop == 'IMPAR' and s % 2 != 0:
        print('Você Ganhou!')
        v += 1
print(f'Total de Vitórias Consecutivas: {v}')

