from math import sin, cos, tan, radians
n = float(input('Digite um ângulo: '))
m = radians(n)
seno = sin(m)
cose = cos(m)
tang = tan(m)
print('seno: {:.2f}, cosseno: {:.2f}, tangente: {:.2f}'.format(seno, cose, tang))