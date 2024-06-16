w = float(input('Insira seu Peso:'))
h = float(input('Insira sua Altura:'))

imc = w/(h * h)

if imc < 18.5:
    print('Abaixo do Peso')
elif 18.5 < imc < 25:
    print('Peso Ideal')
elif 25 < imc < 30:
    print('Sobrepeso')
elif 30 < imc < 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')