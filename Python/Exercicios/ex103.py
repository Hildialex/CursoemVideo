def ficha(nome = 0, gols = 0):
    """
    ->Mostra a ficha do jogador com quantidade de gols
    param nome:(opcional) pega o nome do jogador
    param gols:(opcional) numeros de gols marcados
    return: retorna uma frase com nome e numeros de gols
    """
    if len(nome) == 0:
        nome = '<desconhecido>'
    if len(gols) == 0:
        gols = '0'
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'
jogador = str(input('Nome do jogador:'))
gol = str(input('Número de gols:'))
print(ficha(jogador, gol))
# Solução Guanabara
# def ficha(nome = '<desconhecido>', gols = 0):
#   print (f' O {nome} fez {gols} no campeonato!')
# 
# PRINCIPAL
# n = str(input('Nome Jogador:'))
# g = str(input('Número de gols:'))
# TRANSFORMANDO g EM INTEIRO
# if g.isnumeric():
#   g = int(g)
# else:
#   g = 0
# if n.strip() == '':
#   ficha(gols=g)
# else:  
#   ficha(n, g)