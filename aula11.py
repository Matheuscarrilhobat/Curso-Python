nome = 'Guanabara'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[97;40m'}

print('Olá, Muito prazer em te conhecer,{}{}{}!!!'.format(cores['pretoebranco'], nome, cores['limpa']))