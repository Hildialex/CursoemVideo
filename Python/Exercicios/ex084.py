dado = list()
galera = list()
cont = maior = menor = 0
while True:
    dado.append(str(input('Nome:')))
    dado.append(float(input('Peso:')))
    galera.append(dado[:])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [s/n]?')).strip().upper()[0]
    if resp == 'N':
        break
    dado.clear()
print(f'Foram cadastradas {len(galera)} pessoas.')
#Por nao usar o enumerate acesso direto os campos da lista que esta dentro
for nome, peso in galera:
    if cont == 0:
        maior = menor = peso
        cont += 1
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O Maior peso foi {maior:.1f}Kg.Peso de ', end='')
for nome, peso in galera:
    if peso == maior:
        print(f'{nome}...')
print(f'O Menor peso foi de {menor:.1f}Kg.Peso de ', end='')
for nome, peso in galera:
    if peso == menor:
        print(f'{nome}...')
#Assim eu acesso apenas passando a posição
#for nome, peso in enumerate(galera):
 #   print(nome, peso[1])
