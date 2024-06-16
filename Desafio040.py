nota1 = float(input('Insira a Primeira Nota: '))
nota2 = float(input('Insira a Segunda Nota: '))

media = (nota1 + nota2)/2

if media >= 7:
    print('Aprovado!')
elif media < 5:
    print('Reprovado!')
else:
    print('Recuperação')