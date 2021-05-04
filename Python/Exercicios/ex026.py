frase = str(input('Digite uma frase:'))
qtd = []
num = 0
pri = 0
ult = 0
nova = '-'.join(frase.lower())
for i in nova:
    if i != '-':
        num += 1
    if i == 'a' or i =='á' or i == 'ã':
        qtd.append(i)
        ult = num
num = 0
for j in nova:
    if j != '-':
        num += 1
    if j == 'a' or j =='á' or j =='ã':
        pri = num
        break
print('Letra A aparece: {} vezes\nA primeira vez que aparece é: {}ª posição\nÚltima posição de A: {}ª posição'.format(len(qtd), pri,ult))

#*SOLUÇÃO GUANABARA
# frase = str(input('Digite uma frase:')).lower().strip()
# print('Qtd de a: {}'.format(frase.count('a')))
# print('A primeira a:{}'.format(frase.find('a')+1))
# print('A última a:{}'.format(frase.rfind('a')+1))
#
#
#
# *#