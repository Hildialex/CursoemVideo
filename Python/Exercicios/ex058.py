from random import randint
vezes = num = 0
print('\033[4;33m...Pensei em um número entre 1 e 10...\033[m\nTente adivinhar!')
pc = randint(1,10)
while num != pc:
    vezes += 1
    num = int(input('Digite um palpite:'))
    print('\033[2;31mERROU!\033[mTente novamente!')
print('\033[2;34mPARABÉNS VOCÊ ACERTOU!\033[m\nForam \033[32m{}\033[m tentativas.'.format(vezes))

#*Parte da Solução Guanabara
# acertou = False
# while not acertou:
#   jogador = int(input('Qual palpite?')) 
#   palpite += 1
#   if jogador == computador:
#       acertou = True
#   else:
#       if jogador < computador:
#           print('Mais.. tente novamente.')
#       elif jogador > computador:
#           print('Menos.. tente novament.')
#print('Acertou com {} tentativas'.format(palpites))