n = int(input('Insira o Primeiro termo da PA: '))
r = int(input('Insira a Razão da PA: '))
for c in range(1 , 11):
    tot = n + (c - 1) * r
    print(tot)
print('FIM')