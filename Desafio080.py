lista = list()
for c in range(0, 5):
    n = int(input('Digite um Valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao Final da Lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na Posição {pos} da lista...')
                break
            pos += 1
print('-=' * 30)
print(f'Os Valores digitados em ordem foram {lista}')