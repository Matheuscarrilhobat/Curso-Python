max = 0
min = 999999
for c in range(0, 5):
    peso = float(input('Insira seu Peso: '))
    if peso > max:
        max = peso
    elif peso < min:
        min = peso
print('O Maior peso registrado foi {} e o menor foi {}'.format(max, min))
