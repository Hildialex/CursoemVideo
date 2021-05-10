mul = 0
media = 0
velho = 0
for i in range(0,4):
    nome = str(input('Digite seu nome:'))
    idade = int(input('Digite sua idade:'))
    sexo = str(input('Digite seu sexo (m/f):')).lower()
    media += idade
    if sexo == 'm' and idade >= velho:
        nome_velho = nome
    if sexo == 'f' and idade < 20:
        mul += 1
print('\n O nome do homem mais velho:\033[31m{}\033[m'.format(nome_velho.upper()))
print('\n Quantidade de mulheres com menos de vinte anos:\033[32m{}\033[m'.format(mul))
print('\n Média de idade do grupo:\033[33m{}\033[m'.format(media/4))

