from datetime import date
print('\033[4;32m Alistamento!\033[m')
nasc = int(input('Digite seu ano de nascimento(aaaa):'))
data_atual = date.today()
idade = data_atual.year - nasc
if idade == 18:
    print('Você tem {}{}{} anos\n{}Hora de se alistar!{}'.format('\033[34m', idade, '\033[m', '\033[32m', '\033[m'))
elif idade < 18:
    print('Você tem {}{}{} anos\nAinda faltam {}{}{} anos para se alistar'.format('\033[34m', idade, '\033[m', '\033[31m', 18-idade, '\033[m'))
else:
    print('Você tem {}{}{} anos\nPassou do tempo de se alistar em {}{}{} anos'.format('\033[34m', idade, '\033[m', '\033[31m', idade-18, '\033[m'))
