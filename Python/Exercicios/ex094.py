dados = dict()
lista = list()
listaacima = list()
media = tot = 0
mul = ''
while True:
    nome = str(input('Nome:')).strip()
    sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
    idade = int(input('Idade:'))
    dados['nome'] = nome
    dados['sexo'] = sexo
    dados['idade'] = idade
    lista.append(dados.copy())
    tot += 1
    media += idade
    if sexo == 'F':
        mul += nome + ' '
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]?')).strip().upper()[0]
    if resp == 'N':
        break
media = media/tot
print('=-'*10)
print(f'-> O grupo tem {tot} pessoas.')
print(f'-> A média de idade é {float(media):.2f} anos')
print(f'-> As mulheres cadastradas foram: {mul.upper()}')
print(f'-> Lista das pessoas que estão acima da média:', end='')
for k,v in enumerate(lista):
    if lista[k]['idade'] > media:
        print(f'nome = {lista[k]["nome"]}; sexo = {lista[k]["sexo"]}; idade = {lista[k]["idade"]};')
print('<<<ENCERRADO>>>')
