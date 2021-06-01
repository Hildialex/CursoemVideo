#tuplas são imutáveis
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
#isso dá erro lanche[1] ='Arroz'
print(lanche[-1])
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
#Sem precisar da posição do elemento os outros quando precisar
for comida in lanche:
    print(f'Eu vou comer {comida}')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
#para ordenar em alfabeto
print(sorted(lanche))
a = (2,1,2,3)
b = (12,3,4)
c = a + b
print(c)
#Diferente do anterior
c = b + a
print(c)
#mostra a posição do item na tupla
print(c.index(12))
#mostra a posição do item a partir da posição 1
print(c.index(3, 1))
#para apagar qualquer variavel
del(lanche)
#Quantidade de vezes que aparece o elemento
print(c.count(3))


#lista podem ser modificadas
lanche = []
#adicionar
lanche.append('Cachorro Quente')
lanche.insert(0,'Suco')
#apagar
del lanche[1]
lanche.pop(0)
lanche.insert(0,'Suco')
lanche.remove('Suco')
#criar lista com range
valores = list(range(4,11))
#ordenar
valores.sort()
#inverso
valores.sort(reverse=True)


#dicionario
lanche = {}
lanche['nome'] = 'Hamburguer'
lanche['preco'] = 12.10
print(lanche.items())

pessoas = {'nome': 'Alex', 'idade': 27, 'sexo': 'm'}
print(pessoas.values())
print(pessoas.keys())
#Isso é como o enumerate em tuplas e listas
for k,v in pessoas.items():
    print(f'O {k} é {v}')
estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa:'))
    estado['sigla'] = str(input('Sigla do Estado:'))
   #Assim da erro pq cria um link nao mudando o valor brasil.append(estado)
   #Assim da erro pq não copia brasil.append(estado[:])
    brasil.append(estado.copy())
print(brasil)