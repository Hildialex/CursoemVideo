from random import randint
print('Vamos jogar PAR ou ÍMPAR?')
print('*'*10)
cont = 0
while True:
    computador = randint(0,10)
    jogador = int(input('Digite o valor:'))
    escolha = str(input('Quer PAR ou ÍMPAR?')).strip().upper()[0]
    soma = jogador + computador
    print(f'Você colocou {jogador} e o computador {computador}')
    if soma % 2 == 0 and escolha == 'P':
        cont += 1
        print(f'A soma deu {soma}\nVocê Venceu!')
        print('*'*15)
    else:
        print(f'A soma deu {soma}\nVocê Perdeu!\n')
        break
print(f'Game Over! Foram {cont} vitórias consecutivas!')
print('*'*20)
