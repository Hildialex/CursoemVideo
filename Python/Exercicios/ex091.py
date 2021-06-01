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
# Solução Guanabara
# from time import sleep
# from random import randint
# from operator import itemgetter
# jogo = { 'Jogaodor1' : randint(1,6), 
#           'Jogador2' : randint(1,6),
#           'Jogador3' : randint(1,6),
#           'Jogador4' : randint(1,6)}
# ranking = list()
# for k,v in jogo.items():
#   print(f'{k} tirou {v} no dado.')
#   sleep(1)
# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# for i,v in enumerate(ranking):
#   print(f'{i+1} lugar: {v[0]} com {v[1]}.')
#   sleep(1)
