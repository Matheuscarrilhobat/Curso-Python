num = int(input('Insira um Número Inteiro:'))
inp = int(input('Escolha uma opção:\n1- Binário\n2- Octal\n3- Hexadecimal\n'))

if inp == 1:
    bina = bin(num)
    print(bina[2:])
elif inp == 2:
    octa = oct(num)
    print(octa[2:])
elif inp == 3:
    hexa = hex(num)
    print(hexa[2:])
else:
    print('Número Inválido')