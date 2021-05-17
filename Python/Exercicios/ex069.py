maior = homens = mulheres = 0
while True:
    print('*=*'*10)
    print('Cadastro de Pessoas')
    print('*=*'*10)
    idade = int(input('Informe a idade:'))
    sexo = str(input('Sexo [m/f]:')).strip().upper()[0]
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [m/f]:')).strip().upper()[0]
    if idade < 20 and sexo == 'F':
        mulheres += 1
        if idade >= 18:
            maior += 1
    elif sexo == 'M':
        homens += 1
        if idade >= 18:
            maior += 1
    elif idade >= 18:
        maior += 1
    resp = str(input('Quer cadastrar mais?')).strip().upper()[0]
    while resp not in 'SsNn':
        resp = str(input('Quer cadastrar mais?')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Foram cadastrados:\n{homens} Homens.\n{mulheres} Mulheres abaixo de 20 anos.\n{maior} pessoas acima de 18 anos.')
