dados = {}
gols = list()
jogadores = []
flag = tot = 0
while True:
    nome = str(input('Nome do Jogador:')).strip()
    jogos  =int(input('Partidas jogadas?'))
    for i in range(1, jogos+1):
        gols.append(int(input(f'Qauntos gols na {i}ª partida?')))
        tot += gols[i-1]
    dados['nome'] = nome
    dados['gols'] = gols[:]
    dados['total'] = tot
    jogadores.append(dados.copy())
    gols.clear()
    tot = 0
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]?')).strip().upper()[0]
        print('--'*10)
    if resp == 'N':
        break
print('=-='*25)
print(f'{"cod":<4} {"nome":<20} {"gols":<20} {"total":>10}')
print('--'*30)
for k,v in enumerate(jogadores):
    print(f'{k:<4} {v["nome"]:<20} {v["gols"]} {v["total"]:>20}')
print('--'*30)
while flag != 999:
    flag = int(input('Deseja ver qual jogador?(999 SAIR)'))
    for ke, va in enumerate(jogadores):
        cont = 0
        if ke == flag:
            print(f'O jogador {va["nome"]} fez:')
            while cont < len(va["gols"]):
                print(f'Na {cont+1} partida: {va["gols"][cont]} gols')
                cont += 1
        if flag > len(jogadores) and flag != 999:
            print(f'Chave {flag} não encontrada!', end=' ')
    if flag == 999:
        break