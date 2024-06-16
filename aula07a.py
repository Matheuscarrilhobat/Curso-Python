n1 = int(input('Um Valor: '))
n2 = int(input('Outro Valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \no Produto é {}, \na Divisão é {:.3f}'.format(s,m,d), end=' >>> ')
print('A Divisão Inteira é {}, e a Potência {}'.format(di,e))