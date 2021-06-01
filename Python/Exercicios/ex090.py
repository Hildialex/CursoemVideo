dados = dict()
dados['Nome'] = str(input('Digite o nome:'))
dados['Media'] = float(input(f'A média de {dados["Nome"]}:'))
if dados['Media'] < 7:
    dados['Situacao'] = 'Reprovado'
else:
    dados['Situacao'] = 'Aprovado'
for k,v in dados.items():
    print(f'{k} é igual a {v}')

