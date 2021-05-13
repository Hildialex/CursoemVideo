sexo = ''
while sexo != 'M' or sexo != 'F':
    sexo = str(input('Informe seu sexo (M/F):')).upper()
    if sexo == 'F' or sexo == 'M':
        print('Sexo {} registrado!'.format(sexo))
    else:
        print('Entrada inválida! Apenas F/M')
#Solução Guanabara colocar .strip() para remover espaços
#while sexo not in 'MmFf':
#   sexo = str(input('Dados inválidos!Por favor, digite seu sexo')).strip().upper()[0]
#print('Sexo {} registrado'.format(sexo))