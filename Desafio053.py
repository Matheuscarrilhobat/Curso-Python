pal = input('Insira uma Palavra ou Frase: ')
pal.replace(' ', '')
inv = pal[::-1]
print(inv)
if pal == inv:
    print('Esta Palavra/Frase é um Palíndromo!')
else:
    print('Esta Palavra/Frase NÃO É UM PALÍNDROMO!')