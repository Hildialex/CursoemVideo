import random
al1 = input('Digite o nome do aluno:')
al2 = input('Digite outro nome:')
al3 = input('Digite o terceiro nome:')
al4 = input('Digite o último nome:')
sor = random.randint(0,3)
list = [al1,al2,al3,al4]
print('O aluno escolhido foi : {}'.format(list[sor]))
#Solução do guanabara: random.choice(list)