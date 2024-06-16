valores = list()
max = 0
min = 99999999999999999
for cont in range(0, 5):
    valores.append(int(input('Insira um Valor: ')))
    if valores[cont] > max:
        max = valores[cont]
        posmax = cont
    if valores[cont] < min:
        min = valores[cont]
        posmin = cont
print(f'Menor Valor: {min}, na posição {posmin}')
print(f'Maior Valor: {max}, na posição {posmax}')