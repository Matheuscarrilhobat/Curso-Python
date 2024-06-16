saque = int(input('Quanto Deseja Sacar? '))
resultado = saque
n50 = 0
n20 = 0
n10 = 0
n1 = 0
while True:
    while resultado >= 50:
        resultado -= 50
        n50 += 1
    while resultado >= 20:
        resultado -= 20
        n20 += 1
    while resultado >= 10:
        resultado -= 10
        n10 += 1
    while resultado >= 1:
        resultado -= 1
        n1 += 1
    if resultado == 0:
        print(f'Total {n50} notas de R$50')
        print(f'Total {n20} notas de R$20')
        print(f'Total {n10} notas de R$10')
        print(f'Total {n1} notas de R$1')
        break