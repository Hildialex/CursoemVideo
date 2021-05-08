from random import randint
from time import sleep
print('JOKENPO')
num = int(input('''Faça sua escolha:
[1]-PEDRA
[2]-PAPEL
[3]-TESOURA
Opção:'''))
pc = randint(1,3)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
if num != 1 and num != 2 and num !=3:
    print('Jogada inválida!')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!\n {:=^40}'.format("="))
    if(num == 1 and pc == 1) or ( num == 2 and pc == 2) or (num == 3 and pc ==3):
        #print('Você escolheu PEDRA e o PC PEDRA')
        resp = 'EMPATE'
    elif (num == 1 and pc == 2) or (num == 2 and pc == 3) or (num == 3 and pc == 1):
        resp = 'DERROTA'
    elif (num == 1 and pc == 3) or (num == 2 and pc == 1) or (num == 3 and pc ==2):
        resp = 'VITÓRIA'
    print('Você escolheu \033[31m{}\033[m \nPC escolheu \033[31m{}\033[m\n{:=^40}\nA partida terminou em:\033[33m{}\033[m\n{:=^40}'.format (lista [num-1], lista[pc-1], '=', resp, '='))
