boletim = list()
dados = list ()
nota = list()
flag = media = 0
while True:
    nome = str(input('Nome:')).strip().upper()
    for i in range(1,3):
        nota.append(float(input(f'Nota {i}:')))
    dados.append(nome)
    dados.append(nota[:])
    nota.clear()
    resp = ' '
    while resp not in "SN":
        resp = str(input('Deseja continuar [S/N]?')).strip().upper()[0]
    boletim.append(dados[:])
    dados.clear()
    if resp == "N":
        break
print('=-'*15)
print(f'{"BOLETIM":^30}')
print(f'No. {"NOME":<15} {"MÉDIA":<20}')
print('=-='*15)
for pos, nome in enumerate(boletim):
    media = (nome [1][0]+ nome[1][1])/2
    print(f'{pos}   {nome[0]:<20} {media:<25.1f}')
print('=-='*15)
while flag != 999:
    flag = int(input('Deseja ver as notas da qual aluno?(999 para sair)'))
    for po, n in enumerate(boletim):
        if po == flag: 
            print(f'O aluno {n[0]} tirou {n[1]}')
# sOLUÇÃO GUANABARA
# ficha = list()
# nome = str(input('Nome:'))
# nota1 = float(input('Nota 1:'))
# nota2 = float(input('Nota 2:'))
# media = (nota1+nota2)/2
# ficha.append(nome, [nota1, nota2], media)
# for i, a enumerate(ficha):
#   print(f'{i:<4} {a[0]:<10} {a[2]:8.1f}')
# 