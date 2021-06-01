from datetime import date
dados = dict()
nome = str(input('Nome:'))
nasc = int(input('Ano de Nascimento:'))
atual = date.today().year
ctps = int(input('Carteira de Trabalho (0 se não tiver):'))
if ctps == 0:
    dados['nome'] = nome
    dados['idade'] = (atual - nasc)
    dados['ctps'] = ctps
else:
    dados['nome'] = nome
    dados['idade'] = (atual - nasc)
    dados['ctps'] = ctps
    contrato = int(input('Ano contratação:'))
    salario = float(input('Salário: R$'))
    dados['contratação'] = contrato
    dados['salário'] = salario
    dados['aposentadoria'] = ((contrato + 35) - nasc)
for k,v in dados.items():
    print(f'{k} tem o valor {v}')