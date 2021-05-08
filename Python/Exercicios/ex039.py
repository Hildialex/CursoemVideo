from datetime import date
print('\033[4;32m Alistamento!\033[m')
nasc = int(input('Digite seu ano de nascimento(aaaa):'))
sexo = str(input('Digite seu sexo (f/m):')).lower()
data_atual = date.today().year
idade = data_atual - nasc
if sexo == 'f':
    print('Você é mulher \033[31mNÃO\033[m precisa se alistar')
else:
    if idade == 18:
        print('Você tem {}{}{} anos\n{}Hora de se alistar!{}'.format('\033[34m', idade, '\033[m', '\033[32m', '\033[m'))
    elif idade < 18:
        print('Você tem {}{}{} anos\nAinda faltam {}{}{} anos para se alistar'.format('\033[34m', idade, '\033[m', '\033[31m', 18-idade, '\033[m'))
        print('Seu alistamento será em \033[35m{}\033[m'.format(18-idade+data_atual))
    else:
        print('Você tem {}{}{} anos\nPassou do tempo de se alistar em {}{}{} anos'.format('\033[34m', idade, '\033[m', '\033[31m', idade-18, '\033[m'))
        print('Seu alistamento foi em \033[35m{}\033[m'.format(data_atual-idade+18))