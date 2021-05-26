dado = list()
galera = list()
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
for pos, peso in galera:
    
print(f'Foram cadastradas {len(galera)} pessoas')