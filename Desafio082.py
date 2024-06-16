valores = []
pares = []
impares = []
while True:
    valores.append(int(input('Digite um Número: ')))
    if valores[-1] % 2 == 0:
        pares.append(valores[-1])
    else:
       impares.append(valores[-1])
    resp = str(input('Quer continuar?{S/N]'))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
