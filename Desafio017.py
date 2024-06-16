from math import hypot
n1 = float(input('Digite o comprimento do cateto oposto: '))
n2 = float(input('Digite o comprimento do cateto adjacente: '))
hypo = hypot(n1, n2)
print('O comprimento da hipotenusa é {}'.format(hypo))
