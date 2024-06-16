contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis','dezessete','dezoito', 'dezenove','vinte')
numero = int(input('Digite um Numero entre 0 e 20: '))
allow = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
while numero not in allow:
    numero = int(input('Tente novamente. Digite um Numero entre 0 e 20: '))
print(f'Voce digitou o numero: {contagem[numero]}')