from random import randint
from time import sleep
num = randint(0, 5)
print('Pensando em um número entre 0 e 5 ...')
sleep(2)
ten = int(input('Digite um número que pensei:'))
print('Analisando resposta ...')
sleep(1)
if num == ten:
    print('Você Venceu!')
else:
    print('Você Perdeu! Eu pensei em {}'.format(num))
