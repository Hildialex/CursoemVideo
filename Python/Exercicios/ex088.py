from random import randint
from time import sleep
matriz = list()
print('=-='*15)
print(f'{"MEGA SENA":^40}')
print('=-='*15)
jogadas = int(input('Quantos jogos você quer fazer?'))
print(f'{"=-=-= SORTEANDO":>20} {jogadas} {"JOGOS =--=-":<20}')
sleep(1)
for linha in range(0, jogadas):
    num = []
    for coluna in range(1,7):
        n = randint(1,60)
        if n not in num:
            num.append(n)
    num.sort()
    matriz.append(num[:])
    num.clear()
    print(f'Jogo {linha+1}: {matriz[linha]}')
    sleep(1)
print(f'{" < BOA SORTE! >  ":#^40}')
