mai = 0
hom = 0
mul = 0
while True:
    id = int(input('Insira a Idade: '))
    sx = input('Insira o sexo:')
    sx = sx.upper()
    if id > 18:
        mai += 1
    if sx == 'M':
        hom += 1
    if sx == 'F' and id < 20:
        mul += 1
    end = input('Deseja continuar?[S/N]')
    end = end.upper()
    if end == 'N':
        break
print(f'Total de maiores de idade: {mai}')
print(f'Total de Homens: {hom}')
print(f'Total de Mulheres com menos de 20 anos: {mul}')