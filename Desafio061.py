n = int(input('Insira o Primeiro termo da PA: '))
r = int(input('Insira a Razão da PA: '))
c = 0
tot = 0
while c < 11:
    c = c + 1
    tot = n + (c - 1) * r
    print(tot)
print('FIM')