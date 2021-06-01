dados = dict()
gols = list()
tot = 0
nome = str(input('Nome do Jogador:')).strip()
jogos = int(input(f'Quantas partidas {nome} jogou?'))
for i in range (0, jogos):
    gols.append(int(input(f'Quantos gols na partida {i+1}?')))
    tot += gols[i]
dados['nome'] = nome
dados['gols'] = gols[:]
dados['total'] = tot
print("=-"*10)
print(dados)
print("=-"*10)
for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print("=-"*10)
print(f'O jogador {nome} jogou {jogos} partidas.')
for i in range(0, len(gols)):
    print(f'=> Na partida {i+1}, fez {gols[i]} gols.')
print(f'Foi um total de {tot} gols.')
#da pra usar sum() na lista para somar os valores