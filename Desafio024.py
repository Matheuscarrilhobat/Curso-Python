cid = input('Insira o nome da Cidade: ')
san = cid.split()
pri = san[0].upper()
if pri == 'SANTO':
    print('Cidade começa com Santo')
else:
    print('Cidade não começa com Santo')
