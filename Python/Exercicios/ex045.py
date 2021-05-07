from random import randint
from time import sleep
print('JOKENPO')
num = int(input('Faça sua escolha:\n1-PEDRA\n2-PAPEL\n3-TESOURA\n'))
pc = randint(1,3)
print('JO -- KEN -- PO')
sleep(1)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
if(num == 1 and pc == 1) or ( num == 2 and pc == 2) or (num == 3 and pc ==3):
    #print('Você escolheu PEDRA e o PC PEDRA')
    resp = 'EMPATE'
elif (num == 1 and pc == 2) or (num == 2 and pc == 3) or (num == 3 and pc == 1):
    resp = 'DERROTA'
elif (num == 1 and pc == 3) or (num == 2 and pc == 1) or (num == 3 and pc ==2):
    resp = 'VITÓRIA'
print('Você escolheu \033[31m{}\033[m o PC escolheu \033[31m{}\033[m\nA partida terminou em:\033[33m{}\033[m'.format (lista [num-1], lista[pc-1], resp))
