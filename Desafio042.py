r1 = int(input('Insira o comprimento da reta 1: '))
r2 = int(input('Insira o comprimento da reta 2: '))
r3 = int(input('Insira o comprimento da reta 3: '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r2:
    print('Essas retas formam um triangulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero!')
    elif r1 != r2 != r3 != r1:
        print('Escaleno!')
    else:
        print('Isosceles!')
else:
    print('Não e possivel formar um triangulo.')
