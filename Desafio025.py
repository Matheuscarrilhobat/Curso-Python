nom = input('Insira seu Nome Completo: ')
sil = nom.upper().find('SILVA')
if sil != -1:
    print('Possui Silva no nome')
else:
    print('Não Possui Silva no nome')
