lista = list()
parar = False

while parar != True:
    num = int(input('Digite um Número: '))
    if num not in lista:
        lista.append(num)
    perg = input('Deseja Continuar?[S/N]')
    perg.upper()
    if perg == 'N':
        parar = True
lista.sort()
print(lista)