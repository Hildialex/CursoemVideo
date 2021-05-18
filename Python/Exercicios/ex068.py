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
#* Solução Guanabara
#  while True:
#   ...
#   tipo = ' '
#   while tipo not in 'PI':
#       tipo = str(input('Par ou Impar?')).strip().upper()[0]
#   print(f'Voce jogou {jogador} e PC jogou {computador}.Total {tot}', end = ' ')
#   print('Deu PAR' if tot%2==0 else 'Deu IMPAR')
#   if tipo == 'P':
#       if tot%2==0:
#           print('VENCEU')
#           vit += 1
#       else:
#           print('PERDEU')
#           break
#   elif tipo == 'I':
#       if tot%2==1:
#           print('VENCEU')
#       else:
#           print('PERDEU')
#           break
# #