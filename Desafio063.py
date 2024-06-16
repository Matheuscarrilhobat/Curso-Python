n = int(input('Insira o número de termos a serem mostrados na sequencia de fibonacci: '))
ult = 1
pen = 1
if n == 1 or n == 2:
    print("1")
else:
    count = 3
    print("1")
    print("1")
    while count <= n:
        termo = ult + pen
        pen = ult
        ult = termo
        count += 1
        print(termo)
