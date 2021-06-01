from random import randint
from time import sleep
jogos = list()
jogador = dict()
cont = 1
print('Valores Sorteados')
for i in range(0,4):
    num = randint(1,6)
    jogador['nome'] = 'Jogador ' + str(i+1)
    jogador['valor'] = num
    sleep(1)
    print(f'O {jogador["nome"]} tirou {jogador["valor"]}')
    if i == 0:
        jogos.append(jogador.copy())
    elif num < jogos[len(jogos)-1]['valor']:
        jogos.append(jogador.copy())
    else:
        pos = 0
        while pos < len(jogos):
            if num >= jogos[pos]['valor']:
                jogos.insert(pos, jogador.copy())
                break
            pos += 1
print('Ranking dos Jogadores:')
for k,v in enumerate(jogos):
    print(f'{cont}º lugar: {jogos[k]["nome"]} com {jogos[k]["valor"]}')
    cont += 1
