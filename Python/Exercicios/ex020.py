import random
list =[]
i = 0
while i < 4:
    al = input('Digite o nome do aluno:')
    list.append(al)
    i = i+1
#daqui solução guanabara
random.shuffle(list)
print('A ordem de apresentação será:')
print(list)