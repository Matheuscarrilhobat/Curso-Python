n = int(input('Insira o Primeiro termo da PA: '))
r = int(input('Insira a Razão da PA: '))
t = int(input('Deseja mostrar quantos termos?'))
c = 0
tot = 0
while t != 0:
    c = c + 1
    tot = n + (c - 1) * r
    print(tot)
    if c == t:
        p = int(input('Deseja mostrar mais quantos termos?(digite 0 para encerrar)'))
        t = t + p
        if p == 0:
            t = 0
print('FIM')