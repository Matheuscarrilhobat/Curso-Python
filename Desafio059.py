from time import sleep

n1 = int(input('insira o primeiro valor: '))
n2 = int(input('insira o segundo valor: '))
c = 0
tot = 0
while c != 5:
    print('---MENU---\n[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa')
    c = int(input('Digite um comando: '))
    if c == 1:
        tot = n1 + n2
        print('Total da soma: {}'.format(tot))
        sleep(3)
    elif c == 2:
        tot = n1 * n2
        print('Total da multiplicação: {}'.format(tot))
        sleep(3)
    elif c == 3:
        if n1 > n2:
            print('o Primeiro valor é maior que o segundo')
        elif n1 < n2:
            print('O Segundo valor é maior que o primeiro')
        else:
            print('Os Valores são iguais!')
        sleep(3)
    elif c == 4:
        n1 = int(input('Insira o primeiro valor: '))
        n2 = int(input('Insira o segundo valor: '))
        sleep(3)
