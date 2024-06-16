import random
a1 = input('Insira o nome do primeiro aluno: ')
a2 = input('Insira o nome do segundo aluno: ')
a3 = input('Insira o nome do terceiro aluno: ')
a4 = input('Insira o nome do quarto aluno: ')
lista = [a1, a2 , a3, a4]
random.shuffle(lista)
print('O Primeiro aluno sorteado foi {}\nO Segundo aluno sorteado foi {}\nO Terceiro aluno sorteado foi {}\nO Quarto aluno sorteado foi {}'.format(lista[0], lista[1], lista[2], lista[3]))
