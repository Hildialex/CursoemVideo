print('\033[4;35mMAIOR IDADE!\033[m')
s = 0
for i in range(0,7):
    idade = int(input('Digite sua idade:'))
    if idade >= 21:
        s += 1
print('{} são de maior idade.\n{} são de menor idade.'.format(s, 7-s))

#Aqui lendo pelo nascimento
from datetime import date
soma = 0
data_atual = date.today().year
for i in range(1, 8):
    ano = int(input('Digite o ano de nascimento:'))
    if (data_atual - ano) >= 21:
        soma += 1
print("{} são maoir de idade\n{} são menor de idade".format(soma, 7-soma))