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
    print(f'-> {k} tem o valor {v}')
# Solução Guanabara
# dados = dict()
# dados['nome'] = str(input('Nome:'))
# nasc = int(input('Ano de Nascimento:'))
# dados['idade'] = datetime.now().year - nasc
# dados['ctps'] = int(input('Carteira de trabalho (0 não tem):'))
# if dados['ctps'] != 0:
#   dados['contratação'] = int(input('Ano de Contratação:'))
#   dados['salário'] = float(input('Salário: R$'))
#   dados['aposentadoria'] = ((dados['contratação'] + 35 ) - (datetime.now().year))
# for k,v in dados.items():
#   print(f'-{k} tem o valor {v}')